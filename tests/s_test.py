import os
import unittest
from pyxmp.xmp import XMP

INPUT_WITH_XMP = os.path.join("tests", "images", "image_with_xmp.jpg")
INPUT_WITHOUT_XMP = os.path.join("tests", "images", "image_without_xmp.jpg")
INPUT_WITHOUT_XMP_LARGE_SIZE = os.path.join("tests", "images", "image_without_ns.jpg")

GPANO = "http://ns.google.com/photos/1.0/panorama/"
TPANO = "http://ns.teliportme.com/photos/1.0/panorama/"

class TestXMP(unittest.TestCase):
    def test_with_xmp(self):
        xmp = XMP(INPUT_WITH_XMP, GPANO=GPANO, TPANO=TPANO)
        self.assertEqual(int(xmp.GPANO.FullPanoHeightPixels), 4813)
        self.assertEqual(bool(xmp.GPANO.ExposureLockUsed), True)
        self.assertEqual(xmp.GPANO.StitchingSoftware, 'Panorama 360 iOS')
        self.assertEqual(int(xmp.GPANO.InitialViewHeadingDegrees), 0)
        self.assertEqual(int(xmp.GPANO.CroppedAreaTopPixels), 1559)
        self.assertEqual(int(xmp.GPANO.CroppedAreaLeftPixels), 0)
        self.assertEqual(bool(xmp.GPANO.UsePanoramaViewer), True)
        self.assertEqual(int(xmp.GPANO.CroppedAreaImageHeightPixels), 1696)
        self.assertEqual(int(xmp.GPANO.CroppedAreaImageWidthPixels), 9625)
        self.assertEqual(int(xmp.GPANO.PoseHeadingDegrees), 0)
        self.assertEqual(int(xmp.GPANO.FullPanoWidthPixels), 9625)
        self.assertEqual(int(xmp.GPANO.InitialViewRollDegrees), 0)
        self.assertEqual(int(xmp.GPANO.InitialHorizontalFOVDegrees), 0)
        self.assertEqual(xmp.GPANO.CaptureSoftware, 'Panorama 360')
        self.assertEqual(xmp.GPANO.ProjectionType, 'equirectangular')
        self.assertEqual(xmp.TPANO.RenderType, 'cylinder')
        self.assertEqual(xmp.TPANO.Version, '1.0.19')
        self.assertEqual(int(xmp.TPANO.FrameCount), 23)
        self.assertEqual(int(xmp.TPANO.HorizontalFOV), 360)
        self.assertEqual(int(xmp.TPANO.Build), 2)
        
    def test_without_xmp(self):
        xmp = XMP(INPUT_WITHOUT_XMP, GPANO=GPANO, TPANO=TPANO)
        with self.assertRaises(AttributeError):
            xmp.GPANO.FullPanoWidthPixels

    def test_with_xmp_without_namespaces(self):
        xmp = XMP(INPUT_WITH_XMP)
        with self.assertRaises(AttributeError):
            xmp.GPANO.FullPanoWidthPixels
        
