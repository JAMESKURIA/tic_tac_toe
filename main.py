import turtle as t
import functions as f

f.reset(None, None)
t.onscreenclick(f.mark, btn=1)
t.onscreenclick(f.reset, btn=3)
t.done()
