import frappe
import qrcode
import os
from frappe.utils import now
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import CircleModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask

def get_qr(code, btype):
    print("testing  code")
    filename = str(code) + '.png'
    file_url = "/files/" + filename + "?" + now()
    file_path = os.path.join(frappe.get_site_path("public", "files"), filename)

    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=4, border=1)
    qr.add_data(str(code))
    img = qr.make_image(image_factory=StyledPilImage, color_mask=SolidFillColorMask(), module_drawer=CircleModuleDrawer())
    img.save(file_path)
    return file_url
