#!/usr/bin/env python
import time

from samplebase import SampleBase
from rgbmatrix import graphics

class RunningText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunningText, self).__init__(*args, **kwargs)

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("./7x13.bdf")
        textColor = graphics.Color(255, 255, 0)
        pos = offscreen_canvas.width
        my_text = self.args.text

        while True:
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, 10, textColor, my_text)
            pos -= 1
            if (pos + len < 0):
                pos = offscreen_canvas.width

            time.sleep(0.05)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    simple_square = RunningText()
    if (not simple_square.process()):
        simple_square.print_help()
