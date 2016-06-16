'''
Created on Feb 13, 2014

@author: squinn
'''
import json

encX = json.encoder
encY = json.decoder
encX.c_encode_basestring_ascii()
encY.scanstring("string")

float Angle_radians(float x, float y) const
{ float angle; 
    if (fabs(x)>fabs(y))
        { angle = atan(y/x); if (x<0.0f) angle += PI; }
    else
        { angle = PI*0.5f - (float)atan(x/y);
          if (y<0.0f) angle += PI; }
           if (angle < 0.0f) angle += PI*2;
            if (angle > PI*2) angle -= PI*2;
         return angle; }
     float x_acc = ADC_read(x_axis_channel) // read x axis (horizontal)
     float y_acc = ADC_read(y_axis_channel) // read y axis (vertical)
     x_acc *= 1.0 / 2047; // scale to range -1 .. +1
     y_acc *= 1.0 / 2047;
     angle = angle_radians(x_acc, y_acc); 