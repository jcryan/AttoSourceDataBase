from collections import OrderedDict

HHGData = OrderedDict()
FELData = OrderedDict()

HHGData['hentschel_attosecond_2001']={
       'Duration':[650],
       'PulseEng':[1.5E-10],
      'PhotonEng': [90],
           'type': 'IAP',
         'method': {'generation': 'amplitude gating', 'meterology': 'linear streaking auto-correlation'},
      'Reference': {
           'author':'Hentschel, M.', 
          'journal':'Nature',
              'vol': '414',
             'page': '509-513',
             'year': '2001',
          },
    }

HHGData['sekikawa_nonlinear_2004']={
       'Duration': [950],
       'PulseEng': [2E-9],
      'PhotonEng': [28],
           'type': 'IAP',
         'method': {'generation': 'amplitude gating', 'meterology': 'linear streaking auto-correlation'},
      'Reference': {
           'author': 'Sekikawa, T.', 
          'journal': 'Nature',
              'vol': '432',
             'page': '605-608',
             'year': '2004',
          },
    }

HHGData['sansone_isolated_2006']={
       'Duration': [130],
       'PulseEng': [0.7E-10],
      'PhotonEng': [35],
           'type': 'IAP',
         'method': {'generation': 'polarization gating', 'meterology': 'FROG-CRAB'},
      'Reference': {
           'author': 'Sansone, G.', 
          'journal': 'Science',
              'vol': '314',
             'page': '443-446',
             'year': '2006',
          },
    'Short_Label': '(C)',
    }

HHGData['sola_controlling_2006']={
       'Duration': [260],
       'PulseEng': [70E-12],
      'PhotonEng': [35],
           'type': 'IAP',
         'method': {'generation': 'polarization gating', 'meterology': None},      
      'Reference': {
           'author': 'Sola, I.', 
          'journal': 'Nat. Phys.',
              'vol': '2',
             'page': '319-322',
             'year': '2006',
          },
    }

HHGData['gouliemakis_single-cycle_2008']={
       'Duration': [80],
       'PulseEng': [0.5E-12],
      'PhotonEng': [80],
           'type': 'IAP',
         'method': {'generation': 'amplitude gating', 'meterology': 'FROG-CRAB'},      
      'Reference': {
           'author': 'Gouliemakis, E.', 
          'journal': 'Science',
              'vol': '320',
             'page': '1614-1617',
             'year': '2008',
          },
    }

HHGData['mashiko_double_2008']={
       'Duration': [130],
       'PulseEng': [7E-9],
      'PhotonEng': [38],
           'type': 'IAP',
         'method': {'generation': 'DOG', 'meterology': None},      
      'Reference': {
           'author': 'Mashiko, H.', 
          'journal': 'Phys. Rev. Lett.',
              'vol': '100',
             'page': '103906',
             'year': '2008',
          },
    }

HHGData['feng_generation_2009']={
       'Duration': [260],
       'PulseEng': [230E-12],
      'PhotonEng': [40],
           'type': 'IAP',
         'method': {'generation': 'GDOG', 'meterology': 'FROG-CRAB'},      
      'Reference': {
           'author': 'Feng, X.', 
          'journal': 'Phys. Rev. Lett.',
              'vol': '103',
             'page': '183901',
             'year': '2009',
          },
    }

HHGData['ferrari_high-energy_2010']={
       'Duration': [150],
       'PulseEng': [2.1E-9],
      'PhotonEng': [27],
           'type': 'IAP',
         'method': {'generation': 'ionization gating', 'meterology': 'FROG-CRAB'},      
      'Reference': {
           'author': 'Ferrari, F.', 
          'journal': 'Nat. Photo.',
              'vol': '4',
             'page': '875-879',
             'year': '2010',
          },
    }

HHGData['gilbertson_isolated_2010']={
       'Duration': [160],
       'PulseEng': [170E-12],
      'PhotonEng': [40],
           'type': 'IAP',
         'method': {'generation': 'GDOG', 'meterology': 'FROG-CRAB'},      
      'Reference': {
           'author': 'Gilbertson, S.', 
          'journal': 'Phys. Rev. A',
              'vol': '81',
             'page': '043810',
             'year': '2010',
          },    
    }

HHGData['tzallas_exterme-ultraviolet_2011']={
       'Duration': [1500],
       'PulseEng': [100E-9],
      'PhotonEng': [20],
           'type': 'APT',
         'method': {'generation': 'HHG', 'meterology': 'auto-correlation'},
      'Reference': {
           'author': 'Tzallas, P.', 
          'journal': 'Nat. Phys.',
              'vol': '7',
             'page': '781-784',
             'year': '2011',
          },
    }

HHGData['takahashi_attosecond_2013']={
       'Duration': [375,500],
       'PulseEng': [10E-6,1.3E-6],
      'PhotonEng': [20,30],
           'type': 'IAP',
         'method': {'generation': 'two-color HHG', 'meterology': 'auto-correlation'},      
      'Reference': {
           'author': 'Takahashi, E.', 
          'journal': 'Nat. Comm.',
              'vol': '4',
             'page': '2691',
             'year': '2013',
          },
    }


HHGData['teichmann_0.5-keV_2016']={
       'Duration': [None, None],
       'PulseEng': [2.9E-12,0.9E-12],
      'PhotonEng': [300,350],
           'type': 'IAP',
         'method': {'generation': 'amplitude gating', 'meterology': None},       
      'Reference': {
           'author': 'Teichmann, S.', 
          'journal': 'Nat. Comm.',
              'vol': '7',
             'page': '11493',
             'year': '2016',
          },
    }


HHGData['ossiander_attosecond_2017']={
       'Duration': [130],
       'PulseEng': [0.3E-9],
      'PhotonEng': [113],
           'type': 'IAP',
         'method': {'generation': '', 'meterology': ''},       
      'Reference': {
           'author': 'Ossiander, M.', 
          'journal': 'Nat. Phys.',
              'vol': '',
             'page': '',
             'year': '2017',
          },
    }

HHGData['barillot_towards_2017']={
       'Duration': [680],
       'PulseEng': [100E-12],
      'PhotonEng': [19.6],
           'type': 'IAP',
         'method': {'generation': 'amplitude gating', 'meterology': 'FROG-CRAB'},       
      'Reference': {
           'author': 'Barillot, T.', 
          'journal': 'Chem. Phys. Lett.',
              'vol': '683',
             'page': '38-42',
             'year': '2017',
          },
    }

HHGData['gaumnitz_streaking_2017']={
       'Duration': [47],
       'PulseEng': [3E-12],
      'PhotonEng': [120],
           'type': 'IAP',
         'method': {'generation': 'amplitude gating', 'meterology': 'FROG-CRAB'},             
      'Reference': {
           'author': 'Gaumnitz, T.', 
          'journal': 'Optics Express',
              'vol': '25',
             'page': '27506-27518',
             'year': '2017',
          },
    }

HHGData['li_53-attosecond_2017']={
       'Duration': [53],
       'PulseEng': [5E6 * (200*1.60218E-19)],
      'PhotonEng': [200],
           'type': 'IAP',
         'method': {'generation': 'polarization gating', 'meterology': 'PROOF'},       
      'Reference': {
           'author': 'Li, J.', 
          'journal': 'Nat. Comm.',
              'vol': '8',
             'page': '186',
             'year': '2017',
          },
    }

HHGData['bergues_tabletop_2018']={
       'Duration': [200],
       'PulseEng': [3E-9],
      'PhotonEng': [115],
           'type': 'IAP',
         'method': {'generation': 'ionization gating', 'meterology': None},             
      'Reference': {
           'author': 'Bergues, B.', 
          'journal': 'Optica',
              'vol': '5',
             'page': '237-242',
             'year': '2018',
          },
    }

HHGData['johnson_high-flux_2018']={
       'Duration': [None, None],
       'PulseEng': [2E-12,0.2E-12],
      'PhotonEng': [400,600],
           'type': 'IAP',
         'method': {'generation': 'ionization gating', 'meterology': None},             
      'Reference': {
           'author': 'Johnson, A.', 
          'journal': 'Science Advances',
              'vol': '4',
             'page': '3761',
             'year': '2018',
          },
    }

HHGData['jahn_towards_2019']={
       'Duration': [None],
       'PulseEng': [None],
      'PhotonEng': [None],
           'type': None,
         'method': {'generation': 'relativistic mirror', 'meterology': None},             
      'Reference': {
           'author': 'Jahn, O.', 
          'journal': 'Optica',
              'vol': '6',
             'page': '280-287',
             'year': '2019',
          },
    
    
    }

HHGData['yang_strong-field_2021']={
       'Duration': [82, 241],
       'PulseEng': [100E-12, 500E-12],
      'PhotonEng': [70,45],
           'type': 'IAP',
         'method': {'generation': 'Amplitude Gating', 'meterology': None},                   
      'Reference': {
           'author': 'Yang, Y.', 
          'journal': 'Nat. Comm.',
              'vol': '12',
             'page': '6641',
             'year': '2021',
          },
    }

HHGData['ye_high-flux_2022']={
       'Duration': [166],
       'PulseEng': [51E-12],
      'PhotonEng': [50],
           'type': 'APT',
         'method': {'generation': 'HHG', 'meterology': 'RABBITT'},                         
      'Reference': {
           'author': 'Ye, P.', 
          'journal': 'Ultafast Science',
              'vol': '2022',
             'page': '9823783',
             'year': '2022',
          },
    }

HHGData['wang_ultashort_2024']={
       'Duration': [51],
       'PulseEng': [None],
      'PhotonEng': [100],
           'type': 'IAP',
         'method': {'generation': 'GDOG', 'meterology': 'qPROOF'},                   
      'Reference': {
           'author': 'Wang, X.', 
          'journal': 'Ultafast Science',
              'vol': '5',
             'page': '0080',
             'year': '2024',
          },
    }


HHGData['kretschmar_high-flux_2024']={
       'Duration': [240,240],
       'PulseEng': [3.75E7 * (20*1.60218E-19), 2.8E7 * (33.5*1.60218E-19)],
      'PhotonEng': [20,33.5],
           'type': 'IAP',
         'method': {'generation': 'amplitude gating', 'meterology': 'auto-correlation'},                   
      'Reference': {
           'author': 'Kretschmar, M.', 
          'journal': 'Science Advances',
              'vol': '10',
             'page': 'eadk9605',
             'year': '2024',
          },
    }


FELData['huang_generating_2017']={
       'Duration': [None],
       'PulseEng': [10E-6],
      'PhotonEng': [5600],
           'type': 'IAP',
         'method': {'generation': 'nonlinear compression', 'meterology': None},                         
      'Reference': {
           'author': 'Huang, S.', 
          'journal': 'Phys. Rev. Lett.',
              'vol': '119',
             'page': '154801',
             'year': '2017',
          },
    }

FELData['duris_tunable_2019']={
       'Duration': [480, 280],
       'PulseEng': [25E-6,10E-6],
      'PhotonEng': [570,905],
           'type': 'IAP',
         'method': {'generation': 'Self-modulation', 'meterology': 'Angular Streaking'},                         
      'Reference': {
           'author': 'Duris, J.', 
          'journal': 'Nat. Photo.',
              'vol': '14',
             'page': '30-36',
             'year': '2020',
          },
    }

FELData['maroju_attosecond_2020']={
       'Duration': [210],
       'PulseEng': [16E-6],
      'PhotonEng': [45],
           'type': 'APT',
         'method': {'generation': 'harmonic-lasing of seeded FEL', 'meterology': 'RABBITT-type'},                         
      'Reference': {
           'author': 'Maroju, P.', 
          'journal': 'Nature',
              'vol': '578',
             'page': '386-391',
             'year': '2020',
          },    
    
    }

FELData['franz_terawatt-scale_2024']={
       'Duration': [440],
       'PulseEng': [500E-6],
      'PhotonEng': [865],
           'type': 'IAP',
         'method': {'generation': 'Cathode-modulation with cascaded amplification', 'meterology': 'Angular Streaking'}, 
      'Reference': {
           'author': 'Franz, P.', 
          'journal': 'Nat. Photo.',
              'vol': '18',
             'page': '698-703',
             'year': '2024',
          },
    }

FELData['yan_terawatt-attosecond_2024']={
       'Duration': [None],
       'PulseEng': [180E-6],
      'PhotonEng': [9000],
           'type': 'IAP',
         'method': {'generation': 'non-linear compression', 'meterology': None}, 
      'Reference': {
           'author': 'Yan, J.', 
          'journal': 'Nat. Photo.',
              'vol': '18',
             'page': '1293-1298',
             'year': '2024',
          },
    }

