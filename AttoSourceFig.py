from AttoSourceDB import HHGData, FELData
import matplotlib.pyplot as plt
import numpy as np


class AttoSourcePlot:
    """
    Class for plotting data from the attosecond database. 

    Parameters
    ----------
    source_type : str, optional
        DESCRIPTION. 'HHG' or 'FEL'. The default is 'HHG'.
    pulse_type : str, optional
        DESCRIPTION. 'IAP' or 'APT' The default is 'IAP'.
    x_axis : TYPE, optional
        DESCRIPTION. 'PhotonEng', 'PulseEng', 'Duration', or 'year'. The default is 'PhotonEng'.
    y_axis : TYPE, optional
        DESCRIPTION. 'PhotonEng', 'PulseEng', 'Duration', or 'year'. The default is 'PulseEng'.
    plot_type : TYPE, optional
        DESCRIPTION. 'loglog', 'loglin', 'linlog', or 'linlin'. The default is 'loglog'.

    Returns
    -------
    None.

    """
    def __init__(self, source_type='HHG', pulse_type='IAP', x_axis='PhotonEng', y_axis='PulseEng'):
        p_type = ['IAP', 'APT']
        ax_type = ['PhotonEng', 'PulseEng', 'Duration', 'year']
        
        self.set_source(source_type)
            
        if (pulse_type in p_type):
            self.pulse_type = pulse_type
        else:
            print('Error: pulse_type must be either ' + p_type)
            return
        
        if (x_axis in ax_type):
            self.x=x_axis
            if (x_axis == 'year'):
                for key in self.DB.keys():
                    self.DB[key]['year'] = self.DB[key]['Reference']['year']
        else:
            print('Error: x_axis must be either ' + p_type)
            return
        
        if (y_axis in ax_type):
            self.y=y_axis
            if (y_axis == 'year'):
                for key in self.DB.keys():
                    self.DB[key]['year'] = self.DB[key]['Reference']['year']
        else:
            print('Error: y_axis must be either ' + p_type)
            return
                

    def set_source(self, source_type):
        s_type = ['HHG', 'FEL']
        if (source_type in s_type): 
            if source_type == 'HHG':
                self.DB = HHGData
            elif source_type == 'FEL':
                self.DB = FELData
        else:
            print('Error: source_type must be either ' + s_type)
            return
        
    def plot(self, plot_labels='a', plot_markers='bo', x_scale='log', y_scale='log', new_fig=False):
        
        label_index = ord(plot_labels[0])
        
        def p_label(label,index):
            out = '('
            for ind,c in enumerate(label):
                out+= chr(index)
            out+=')'
            return out
        
        if new_fig or (not hasattr(self,'fig')):
            self.fig = plt.figure(num=1, figsize=(5, 6),layout='constrained')
            self.ax = self.fig.add_subplot(111)
            self.cite_key=''
            self.texts = []
        
        for key in self.DB:
            if (None not in self.DB[key][self.x]) and (None not in self.DB[key][self.y]):
                if self.DB[key]['type'] == self.pulse_type:
        
                    point_label=p_label(plot_labels, label_index)
                    
                    x=self.DB[key][self.x]
                    y=self.DB[key][self.y]
                    
                    if x_scale == 'log' and y_scale == 'log':
                        self.ax.loglog(x,y, plot_markers, label=(point_label+' ['+self.DB[key]['Reference']['author'][:-4]+', ('+self.DB[key]['Reference']['year']+')]'))
                    elif x_scale == 'lin' and y_scale == 'lin':
                        self.ax.plot(x,y, plot_markers, label=(point_label+' ['+self.DB[key]['Reference']['author'][:-4]+', ('+self.DB[key]['Reference']['year']+')]'))                                              
                    for xy in  zip(x,y): 
                        self.texts.append(self.ax.annotate( point_label, xy=xy, textcoords='data'))     
                    label_index+=1
                    self.cite_key+=(key+', ')
        return
    
    def emblish(self):
        
        if (not hasattr(self,'fig')):
            print('No figure to embelish')
            return
        
        import xraydb as xdb
        x_lim = plt.xlim()
        y_lim = plt.ylim()
        
        E_ph = np.logspace(1.5, 4,100)
        E_min = np.ones_like(E_ph)
        for ele in ['He', 'C', 'O', 'Ne', 'Ar', 'Kr', 'Xe', 'Cl', 'Br', 'I', 'S']:
            mu = xdb.mu_chantler(element=ele, energy=E_ph, photo=True)
            cs = mu * 1.66054e-24 * xdb.atomic_mass(ele)
            E_sat = (1E-4)**2 / cs * (1.602E-19 * E_ph)
            E_min = [min(x,y) for x,y in zip(E_min,E_sat)]
            
        p = np.polyfit(np.log10(E_ph), np.log10(E_min), 2)
        E_ph2 = np.logspace(0.5, 4.3,100)
        self.ax.fill_between(E_ph2, 10**(np.polyval(p, np.log10(E_ph2))-2), y2=1, interpolate=True, color='blue', alpha=0.3)
        self.ax.annotate( 'Nonlinear Interactions', xy=(400,1E-9), rotation=37, alpha=0.3, color='blue')
        self.ax.plot(E_ph2, 1E12*E_ph**-8, 'k', alpha=0.3)
        plt.xlim(x_lim)
        plt.ylim(y_lim)
