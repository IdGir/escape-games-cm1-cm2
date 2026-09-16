"""reseau.py — Mode « salle informatique » : IP locale + QR code (Phase I)."""
import io
import socket


def ip_locale():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("10.255.255.255", 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip


def url_acces(port, ip=None):
    return f"http://{ip or ip_locale()}:{port}"


def qr_svg(donnees):
    try:
        import qrcode
        import qrcode.image.svg
        img = qrcode.make(donnees, image_factory=qrcode.image.svg.SvgPathImage,
                          box_size=11, border=2)
        b = io.BytesIO()
        img.save(b)
        return b.getvalue().decode("utf-8")
    except Exception:
        return ""
