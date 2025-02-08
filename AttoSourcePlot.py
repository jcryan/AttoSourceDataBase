from AttoSourceDB import HHGData, FELData
import matplotlib.pyplot as plt
import numpy as np

cite_key = []

fig = plt.figure()
ax = fig.add_subplot(111)

i=97
j=97
prev_label=[(0,0)]
for keys in HHGData:
    if (None not in HHGData[keys]['PhotonEng']) and (None not in HHGData[keys]['PulseEng']):
        if HHGData[keys]['type'] == 'IAP':
            
            label='('+chr(i)+')'
            x=HHGData[keys]['PhotonEng']
            y=HHGData[keys]['PulseEng']
            ax.loglog(x,y, 'bo', label=(label+' ['+HHGData[keys]['Reference']['author'][:-4]+', ('+HHGData[keys]['Reference']['year']+')]'))
            for xy in  zip(x,y): 
                is_close = np.isclose(prev_label, xy, rtol=1E-1)
                
                if True in (is_close[:,0]*is_close[:,1]):
                    xy_pos=tuple(np.array(xy)*np.array((1.1,0.5)))
                else:
                    xy_pos=tuple(np.array(xy)*np.array((0.8,2)))              
                ax.annotate( label, xy=xy_pos, textcoords='data')
                prev_label.append(xy_pos)
            
            i+=1
            cite_key.append(keys)

        elif HHGData[keys]['type'] == 'APT':
            
            label='('+chr(j)+chr(j)+')'
            x=HHGData[keys]['PhotonEng']
            y=HHGData[keys]['PulseEng']
            ax.loglog(x,y, 'bv', label=(label+' ['+HHGData[keys]['Reference']['author'][:-4]+', ('+HHGData[keys]['Reference']['year']+')]'))
            for xy in  zip(x,y): 
                ax.annotate( label, xy=tuple(np.array(xy)*np.array((1,2))), textcoords='data')
            j+=1
            cite_key.append(keys)        
i=65
j=65
for keys in FELData:
    if (None not in FELData[keys]['PhotonEng']) and (None not in FELData[keys]['PulseEng']):
        if FELData[keys]['type'] == 'IAP':
            label='('+chr(i)+')'
            x=FELData[keys]['PhotonEng']
            y=FELData[keys]['PulseEng']
            ax.loglog(x,y, 'ro', label=(label+' ['+FELData[keys]['Reference']['author'][:-4]+']'))
            for xy in  zip(x,y): 
                ax.annotate( label, xy=tuple(np.array(xy)*np.array((1,2))), textcoords='data')
            i+=1
            cite_key.append(keys)
            
        elif FELData[keys]['type'] == 'APT':
            label='('+chr(j)+chr(j)+')'
            x=FELData[keys]['PhotonEng']
            y=FELData[keys]['PulseEng']
            ax.loglog(x,y, 'rv', label=(label+' ['+FELData[keys]['Reference']['author'][:-4]+']'))
            for xy in  zip(x,y): 
                ax.annotate( label, xy=tuple(np.array(xy)*np.array((1,2))), textcoords='data')
            j+=1
            cite_key.append(keys)


#ax.legend()





