
import base64

im_filename = 'leibniz_im.gif'
im_variable_name = 'leibniz'
py_filename = 'leibniz_image_embedded.py'

with open('leibniz_im.gif','rb') as f:
    str64 = base64.b64encode(f.read())

with open('leibniz_image_embedded.py','w') as f:
    f.write('%s="%s"'%('leibniz',str64))

from PIL import Image,ImageTk
import cStringIO
import base64

from embeddedImage import background 
# or copy paste the background variable found in embeddedImage.py



im_filename = 'ode_icon.ico'
im_variable_name = 'icone'
py_filename = 'icon_embedded.py'

with open('ode_icon.ico','rb') as f:
    str64 = base64.b64encode(f.read())

with open('icon_embedded.py','w') as f:
    f.write('%s="%s"'%('icone',str64))

from PIL import Image,ImageTk
import cStringIO
import base64

from icon_embedded import icone
from leibniz_image_embedded import leibniz
# or copy paste the background variable found in embeddedImage.py
icon = Image.open(cStringIO.StringIO(base64.b64decode(icone)))
leibniz_im = Image.open(cStringIO.StringIO(base64.b64decode(leibniz)))

