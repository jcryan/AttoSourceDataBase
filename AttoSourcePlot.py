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
        DESCRIPTION. 'PhotonEnergy', 'PulseEnergy', 'Duration', or 'year'. The default is 'PhotonEnergy'.
    y_axis : TYPE, optional
        DESCRIPTION. 'PhotonEnergy', 'PulseEnergy', 'Duration', or 'year'. The default is 'PulseEnergy'.
    plot_type : TYPE, optional
        DESCRIPTION. 'loglog', 'loglin', 'linlog', or 'linlin'. The default is 'loglog'.

    Returns
    -------
    None.

    """
    def __init__(self, source_type='HHG', pulse_type='IAP', x_axis='PhotonEnergy', y_axis='PulseEnergy'):
        p_type = ['IAP', 'APT']
        ax_type = ['PhotonEnergy', 'PulseEnergy', 'Duration', 'year']
        
        if (pulse_type in p_type):
            self.pulse_type = pulse_type
        else:
            print('Error: pulse_type must be either ' + p_type)
            return
        
        if (x_axis in ax_type):
            self.x=x_axis
        else:
            print('Error: x_axis must be either ' + p_type)
            return
        
        if (y_axis in ax_type):
            self.y=y_axis
        else:
            print('Error: y_axis must be either ' + p_type)
            return
        
        self.set_source(source_type)
                
    def _get_year(self):
        if (self.x == 'year') or (self.y == 'year'):
            for key in self.DB.keys():
                self.DB[key]['year'] = [int(self.DB[key]['Reference']['year'])]*len(self.DB[key]['Duration'])
        return
        
    def set_source(self, source_type):
        """
        Change source type between 'FEL' or 'HHG'

        Parameters
        ----------
        source_type : TYPE
            'HHG' or 'FEL'.

        """
        s_type = ['HHG', 'FEL']
        if (source_type in s_type): 
            if source_type == 'HHG':
                self.DB = HHGData
            elif source_type == 'FEL':
                self.DB = FELData
            self._get_year()
        else:
            print('Error: source_type must be either ' + s_type)
            return
        
    def plot(self, plot_labels='a', plot_markers='bo', x_scale='log', y_scale='log', new_fig=False):
        """
        Plot the data in the database

        Parameters
        ----------
        plot_labels : string, optional
            Label for legend. The default is 'a'.
        plot_markers : string, optional
            plot marker type. The default is 'bo'.
        x_scale : string, optional
            x-axis scale, 'linear' or 'log'. The default is 'log'.
        y_scale : string, optional
            y-axis scale, 'linear' or 'log'. The default is 'log'.
        new_fig : bool, optional
            Create a new figure, or plot plot on the existing figure. If there is no existing figure, a new figure is created. The default is False.

        Returns
        -------
        out : TYPE
            DESCRIPTION.

        """
        
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
                    
                    self.ax.plot(x,y, plot_markers, label=(point_label+' ['+self.DB[key]['Reference']['author'][:-4]+', ('+self.DB[key]['Reference']['year']+')]'))                                              
                    for xy in  zip(x,y): 
                        self.texts.append(self.ax.annotate( point_label, xy=xy, textcoords='data'))     
                    label_index+=1
                    self.cite_key+=(key+', ')
        self.ax.set_xscale(x_scale)
        self.ax.set_yscale(y_scale)
        return
    
    def decorate(self):
        
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
