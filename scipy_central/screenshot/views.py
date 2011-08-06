from django.http import HttpResponse
from django.utils import simplejson
import models

from scipy_central.screenshot.forms import ScreenshotForm

def add_screenshot(request):
    """
    Received POST request to add a new screenshot.
    """
    img_form = ScreenshotForm(request.POST, request.FILES)
    if img_form.is_valid():

        #TODO: CODE HERE TO PREVENT spaces;
        #slugify the file name

        img = models.Screenshot(img_file_raw=img_form.\
                                              cleaned_data['spc_image_upload'])
        img.save()
        msg = ('<div class="spc-item-upload-success" style="float: left;">'
               'Upload successful. Insert the image in your description as'
               '&nbsp;&nbsp;&nbsp; <tt>:image:`%s`</tt><br>'
               'Want a <b>smaller</b> image? e.g. scale down to 40%%: &nbsp;&nbsp;&nbsp;'
               '<tt>:image:`%s;40`</tt><br></div>') %\
                            (img.img_file_raw.name.partition('/')[2],
                             img.img_file_raw.name.partition('/')[2])
        return HttpResponse(msg)
    else:
        msg = ('<div class="spc-field-error" style="float: left; font-style: '
               'italic;">%s</div>') % img_form.errors.get('spc_image_upload')[0]
        return HttpResponse(msg)
