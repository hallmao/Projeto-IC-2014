
import base64

im_filename = 'Euler.png'
im_variable_name = 'euler'
py_filename = 'euler_image_embedded.py'

with open(im_filename,'rb') as f:
    str64 = base64.b64encode(f.read())

with open(py_filename,'w') as f:
    f.write('%s="%s"'%(im_variable_name,str64))

from PIL import Image,ImageTk
import cStringIO
import base64

##from embeddedImage import background 
### or copy paste the background variable found in embeddedImage.py
##
##
##
##im_filename = 'ode_icon.ico'
##im_variable_name = 'icone'
##py_filename = 'icon_embedded.py'
##
##with open('ode_icon.ico','rb') as f:
##    str64 = base64.b64encode(f.read())
##
##with open('icon_embedded.py','w') as f:
##    f.write('%s="%s"'%('icone',str64))

from PIL import Image,ImageTk
import cStringIO
import base64

#from icon_embedded import icone
from euler_image_embedded import euler
# or copy paste the background variable found in embeddedImage.py
#icon = Image.open(cStringIO.StringIO(base64.b64decode(icone)))
euler_im = Image.open(cStringIO.StringIO(base64.b64decode(euler)))

