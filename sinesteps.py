# thanks to https://github.com/fwswdev
import math

TARGET_FILE=r'output.pwl' # why the fuck is there an r after the = sign? it means raw string.
BOOL_DISPLAY_FILE_CONTENTS=True
TOTAL_TIME=1/60.0
FREQUENCY=60.0
# STEP_TIME=0.0001
PEAK_VOLTAGE=240*1.414
NUM_STEPS=256
step_time=TOTAL_TIME/NUM_STEPS
sin_factor=2*math.pi*FREQUENCY*step_time
step_time=TOTAL_TIME/NUM_STEPS

tmp='' # output

for x in range(NUM_STEPS):
    tmp+='%f \t %f\n' % (x * step_time,math.fabs(math.sin(x*sin_factor)*PEAK_VOLTAGE))

with open(TARGET_FILE,'w') as f:
    f.write(tmp)

if(BOOL_DISPLAY_FILE_CONTENTS):
    print '========= File Contents: ==========\n'
    print tmp
    print '========= EOF ==========\n\n'

print  "File Created: '%s'"  % (TARGET_FILE)
