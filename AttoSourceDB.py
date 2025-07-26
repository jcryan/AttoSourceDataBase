from collections import OrderedDict

HHGData = OrderedDict()
FELData = OrderedDict()

HHGData['hentschel_attosecond_2001']={
       'Duration':[650],
       'PulseEnergy':[1.5E-10],
      'PhotonEnergy': [90],
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
       'PulseEnergy': [2E-9],
      'PhotonEnergy': [28],
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
       'PulseEnergy': [0.7E-10],
      'PhotonEnergy': [35],
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
       'PulseEnergy': [70E-12],
      'PhotonEnergy': [35],
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

HHGData['goulielmakis_single-cycle_2008']={
       'Duration': [80],
       'PulseEnergy': [0.5E-12],
      'PhotonEnergy': [80],
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
       'PulseEnergy': [7E-9],
      'PhotonEnergy': [38],
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
       'PulseEnergy': [230E-12],
      'PhotonEnergy': [40],
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

HHGData['mashiko_exterme_2009']={
       'Duration': [107],
       'PulseEnergy': [None],
      'PhotonEnergy': [70],
           'type': 'IAP',
         'method': {'generation': 'DOG', 'meterology': 'FROG-CRAB'},      
      'Reference': {
           'author': 'Mashikp, H.', 
          'journal': 'Opt. Lett.',
              'vol': '34',
             'page': '3337-3339',
             'year': '2009',
          },
    }

HHGData['ferrari_high-energy_2010']={
       'Duration': [150],
       'PulseEnergy': [2.1E-9],
      'PhotonEnergy': [27],
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
       'PulseEnergy': [170E-12],
      'PhotonEnergy': [40],
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

HHGData['tzallas_extreme-ultraviolet_2011']={
       'Duration': [1500],
       'PulseEnergy': [100E-9],
      'PhotonEnergy': [20],
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
       'PulseEnergy': [10E-6,1.3E-6],
      'PhotonEnergy': [20,30],
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

HHGData['teichmann_05-kev_2016']={
       'Duration': [None, None],
       'PulseEnergy': [2.9E-12,0.9E-12],
      'PhotonEnergy': [300,350],
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
       'PulseEnergy': [0.3E-9],
      'PhotonEnergy': [113],
           'type': 'IAP',
         'method': {'generation': 'amplitude gating', 'meterology': 'FROG-CRAB'},       
      'Reference': {
           'author': 'Ossiander, M.', 
          'journal': 'Nat. Phys.',
              'vol': '13',
             'page': '280-285',
             'year': '2017',
          },
    }

HHGData['barillot_towards_2017']={
       'Duration': [680],
       'PulseEnergy': [100E-12],
      'PhotonEnergy': [19.6],
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

HHGData['cousin_attosecond_2017']={
       'Duration': [23],
       'PulseEnergy': [5.6E5 * (300*1.60218E-19)],
      'PhotonEnergy': [300],
           'type': 'IAP',
         'method': {'generation': 'ionization gating', 'meterology': 'FROG-CRAB'},             
      'Reference': {
           'author': 'Cousins, S.', 
          'journal': 'Phys. Rev. X',
              'vol': '7',
             'page': '041030',
             'year': '2017',
          },
    }

HHGData['gaumnitz_streaking_2017']={
       'Duration': [47],
       'PulseEnergy': [3E-12],
      'PhotonEnergy': [120],
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
       'PulseEnergy': [5E6 * (200*1.60218E-19)],
      'PhotonEnergy': [200],
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
       'PulseEnergy': [3E-9],
      'PhotonEnergy': [115],
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
       'PulseEnergy': [2E-12,0.2E-12],
      'PhotonEnergy': [400,600],
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
       'PulseEnergy': [None],
      'PhotonEnergy': [None],
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
       'PulseEnergy': [100E-12, 500E-12],
      'PhotonEnergy': [70,45],
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
       'PulseEnergy': [51E-12],
      'PhotonEnergy': [50],
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

HHGData['xue_gigawatt-class_2022']={
       'Duration': [226],
       'PulseEnergy': [24E-6],
      'PhotonEnergy': [70],
           'type': 'IAP',
         'method': {'generation': 'Waveform Synthesizer', 'meterology': 'FROG-CRAB'},                         
      'Reference': {
           'author': 'Xue, B.', 
          'journal': 'Optica',
              'vol': '9',
             'page': '360-363',
             'year': '2022',
          },
    }

HHGData['kretschmar_compact_2024']={
       'Duration': [240,240],
       'PulseEnergy': [3.75E7 * (20*1.60218E-19), 2.8E7 * (33.5*1.60218E-19)],
      'PhotonEnergy': [20,33.5],
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

HHGData['wang_ultrashort_2024']={
       'Duration': [51],
       'PulseEnergy': [None],
      'PhotonEnergy': [100],
           'type': 'IAP',
         'method': {'generation': 'GDOG', 'meterology': 'qPROOF'},                   
      'Reference': {
           'author': 'Wang, X.', 
          'journal': 'Ultrafast Science',
              'vol': '4',
             'page': '0080',
             'year': '2024',
          },
    }

FELData['huang_generating_2017']={
       'Duration': [None],
       'PulseEnergy': [10E-6],
      'PhotonEnergy': [5600],
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

FELData['marinelli_experimental_2017']={
       'Duration': [None],
       'PulseEnergy': [5E-6],
      'PhotonEnergy':[5600],
           'type': 'IAP',
         'method': {'generation': 'slotted foil beam shaping', 'meterology': None},    
      'Reference': {
           'author': 'Marinelli, A.', 
          'journal': 'Appl. Phys. Lett.',
              'vol': '111',
             'page': '151101',
             'year': '2017',
        },
    }


FELData['hartmann_attosecond_2018']={
    'Duration': [800],
    'PulseEnergy': [64E-6],
   'PhotonEnergy':[1180],
        'type': 'IAP',
      'method': {'generation': 'slotted foil beam shaping', 'meterology': 'angular streaking'},    
   'Reference': {
        'author': 'Hartmann, N.', 
       'journal': 'Nat. Photon.',
           'vol': '12',
          'page': '215-220',
          'year': '2018',
     },
 }

FELData['duris_tunable_2020']={
       'Duration': [480, 280],
       'PulseEnergy': [25E-6,10E-6],
      'PhotonEnergy': [570,905],
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

FELData['malyzhenkov_single-_2020']={
       'Duration': [None],
       'PulseEnergy': [1.3E-6],
      'PhotonEnergy': [7360],
           'type': 'IAP',
         'method': {'generation': 'Nonlinear compression', 'meterology': None},                         
      'Reference': {
           'author': 'Malyzhenkov, A.', 
          'journal': 'Phys. Rev. Res.',
              'vol': '2',
             'page': '042018(R)',
             'year': '2020',
          },    
    
    }
FELData['maroju_attosecond_2020']={
       'Duration': [210],
       'PulseEnergy': [16E-6],
      'PhotonEnergy': [45],
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

FELData['prat_coherent_2023']={
       'Duration': [400, 200],
       'PulseEnergy': [20E-6,5E-6],
      'PhotonEnergy': [642,1111],
           'type': 'IAP',
         'method': {'generation': 'nonlinear compression', 'meterology': 'estimated from longitudianl phase space measurement'}, 
      'Reference': {
           'author': 'Prat, E.', 
          'journal': 'APL Photonics',
              'vol': '8',
             'page': '111302',
             'year': '2023',
          },
    }

FELData['franz_terawatt-scale_2024']={
       'Duration': [440],
       'PulseEnergy': [500E-6],
      'PhotonEnergy': [865],
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
       'PulseEnergy': [180E-6],
      'PhotonEnergy': [9000],
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
