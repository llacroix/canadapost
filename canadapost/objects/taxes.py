from .base import CPObject


class Taxes(CPObject):
    _name = 'taxes'

    def __init__(self, gst, gst_percent, pst, hst):
        self.gst = gst
        self.gst_percent = gst_percent
        self.pst = pst
        self.hst = hst

    @classmethod
    def from_xml(cls, node, ns):
        gst = CPObject.get_float(node, 'cp:gst', ns)
        gst_percent = float(
            node.find('cp:gst', namespaces=ns).attrib['percent']
        )
        hst = CPObject.get_float(node, 'cp:hst', ns)
        pst = CPObject.get_float(node, 'cp:pst', ns)

        return Taxes(
            gst,
            gst_percent,
            pst,
            hst
        )
