#coding:utf-8
import os
import random
import re
import tempfile
from cStringIO import StringIO

try:
    import Image
    import ImageDraw
    import ImageFont
except ImportError,e:
	from PIL import Image, ImageDraw, ImageFont

from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404

try:
    # Python >= 2.6
    import json
except ImportError:
    from django.utils import simplejson as json

from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST

from captcha.conf import settings
from captcha.helpers import generate_captcha_store
from captcha.models import CaptchaStore

NON_DIGITS_RX = re.compile('[^\d]')


def captcha_image(request, key):
    store = get_object_or_404(CaptchaStore, hashkey=key)
    text = store.challenge

    if settings.CAPTCHA_FONT_PATH.lower().strip().endswith('ttf'):
	font = ImageFont.truetype(settings.CAPTCHA_FONT_PATH, settings.CAPTCHA_FONT_SIZE)
    else:
        font = ImageFont.load(settings.CAPTCHA_FONT_PATH)

    size = font.getsize(text)
    size = (size[0] * 2, int(size[1] * 1.2))
    image = Image.new('RGB', size, settings.CAPTCHA_BACKGROUND_COLOR)
    try:
        PIL_VERSION = int(NON_DIGITS_RX.sub('', Image.VERSION))
    except:
        PIL_VERSION = 116
    xpos = 2

    charlist = []
    for char in text:
        if char in settings.CAPTCHA_PUNCTUATION and len(charlist) >= 1:
            charlist[-1] += char
        else:
            charlist.append(char)
    for char in charlist:
        fgimage = Image.new('RGB', size, settings.CAPTCHA_FOREGROUND_COLOR)
        tuple_temp = (font.getsize(' %s ' % char)[0],8+font.getsize(' %s ' % char)[1]) #changed by lxp 20150209
	
	charimage = Image.new('L', tuple_temp, '#000000')
        chardraw = ImageDraw.Draw(charimage)
        chardraw.text((0, 0), ' %s ' % char, font=font, fill='#ffffff')
        if settings.CAPTCHA_LETTER_ROTATION:
            if PIL_VERSION >= 116:
                charimage = charimage.rotate(random.randrange(*settings.CAPTCHA_LETTER_ROTATION), expand=0, resample=Image.BICUBIC)
            else:
                charimage = charimage.rotate(random.randrange(*settings.CAPTCHA_LETTER_ROTATION), resample=Image.BICUBIC)
        charimage = charimage.crop(charimage.getbbox())
        maskimage = Image.new('L', size)

        maskimage.paste(charimage, (xpos, 0, xpos + charimage.size[0], charimage.size[1]))
        size = maskimage.size
        image = Image.composite(fgimage, image, maskimage)
        xpos = xpos + 2 + charimage.size[0]

    image = image.crop((0, 0, xpos + 1, size[1]))
    draw = ImageDraw.Draw(image)

    for f in settings.noise_functions():
        draw = f(draw, image)
    for f in settings.filter_functions():
        image = f(image)

    out = StringIO()
    image.save(out, "PNG")
    out.seek(0)

    response = HttpResponse()
    response['Content-Type'] = 'image/png'
    response.write(out.read())
    return response

def captcha_audio(request, key):
    if settings.CAPTCHA_FLITE_PATH:
        store = get_object_or_404(CaptchaStore, hashkey=key)
        text = store.challenge
        if 'captcha.helpers.math_challenge' == settings.CAPTCHA_CHALLENGE_FUNCT:
            text = text.replace('*', 'times').replace('-', 'minus')
        else:
            text = ', '.join(list(text))
        path = str(os.path.join(tempfile.gettempdir(), '%s.wav' % key))
        cline = '%s -t "%s" -o "%s"' % (settings.CAPTCHA_FLITE_PATH, text, path)
        os.popen(cline).read()
        if os.path.isfile(path):
            response = HttpResponse()
            f = open(path, 'rb')
            response['Content-Type'] = 'audio/x-wav'
            response.write(f.read())
            f.close()
            os.unlink(path)
            return response
    raise Http404

@require_POST
def captcha_reload_ajax(request):
    store = generate_captcha_store()
    data = {
        'key': store.hashkey,
        'image_url': reverse(
            'captcha-image',
            kwargs=dict(key=store.hashkey)
        )
    }
    return HttpResponse(
        json.dumps(data),
        mimetype='application/json'
    )


