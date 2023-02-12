import time

hour=time.strftime('%H')
minutes=time.strftime('%M')

if int(hour)>=19:
    print('Es hora de irse a casa')
else:
    print('Solo faltan',18-int(hour), 'y', 59-int(minutes),'para irse a casa')