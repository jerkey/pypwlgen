# thanks to https://github.com/fwswdev
import math

TARGET_FILE=r'output.pwl' # why the fuck is there an r after the = sign?
BOOL_DISPLAY_FILE_CONTENTS=True
TOTAL_TIME=1/60.0
FREQUENCY=60.0
STEP_TIME=0.0001
PEAK_VOLTAGE=240*1.414
num_steps=int(TOTAL_TIME/STEP_TIME)
sin_factor=2*math.pi*FREQUENCY*STEP_TIME
step_time=TOTAL_TIME/num_steps

tmp='' # output

for x in range(num_steps):
    tmp+='%f \t %f\n' % (x * step_time,math.fabs(math.sin(x*sin_factor)*PEAK_VOLTAGE))

with open(TARGET_FILE,'w') as f:
    f.write(tmp)

if(BOOL_DISPLAY_FILE_CONTENTS):
    print '========= File Contents: ==========\n'
    print tmp
    print '========= EOF ==========\n\n'

print  "File Created: '%s'"  % (TARGET_FILE)
