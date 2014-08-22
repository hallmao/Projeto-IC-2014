
import base64

im_filename = 'leibniz_im.gif'
im_variable_name = 'background'
py_filename = 'leibniz_image_embedded.py'

with open('leibniz_im.gif','rb') as f:
    str64 = base64.b64encode(f.read())

with open('leibniz_image_embedded.py','w') as f:
    f.write('%s="%s"'%(im_variable_name,str64))

from PIL import Image,ImageTk
import cStringIO
import base64

from embeddedImage import background 
# or copy paste the background variable found in embeddedImage.py
leibniz_im = Image.open(cStringIO.StringIO(base64.b64decode(background)))


im_filename = 'ode_icon.ico'
im_variable_name = 'background'
py_filename = 'icon_embedded.py'

with open('ode_icon.ico','rb') as f:
    str64 = base64.b64encode(f.read())

with open('icon_embedded.py','w') as f:
    f.write('%s="%s"'%(im_variable_name,str64))

from PIL import Image,ImageTk
import cStringIO
import base64

from embeddedImage import background
# or copy paste the background variable found in embeddedImage.py
icon_im = Image.open(cStringIO.StringIO(base64.b64decode(background)))

