import streamlit as st
from streamlit_option_menu import option_menu
import os

st.set_page_config(layout="wide")
st.title('Villum Center for Hybrid Quantum Materials and Devices')


selected=option_menu('',['Research Facilities','Group members','Gallery','Openings'],\
                      orientation='horizontal', icons=['clipboard', 'person','collection','envelope'])
if selected=='Group members':
    
    st.header('Principal Investigators')
    st.subheader('Prof. Yong P. Chen')
    col0,col1,col1a,col2=st.columns([1,4,1,22],gap="large")

    with col1:
        st.image('Images/chen.png',width=180)
    with col2:
        st.markdown('My lab exploits quantum physics to manipulate electrons, \
        atoms, spins and photons in various materials and artificial systems, with the aim to uncover \
        novel quantum phenomena and new states of matter, and to explore applications in quantum devices\
        (such as quantum information and quantum computation devices), nanotechnology (such as nanoelectronics \
        and nanosensors) and energy.')
        st.markdown('[Google Scholar](https://scholar.google.com/citations?user=9EBAemEAAAAJ&hl=en)')

        st.markdown('**Email**: <yongchen@phys.au.dk>')
    



    st.subheader('Dr. Richard Balog')
    col0,col1,col1a,col2=st.columns([1,4,1,22],gap="large")

    with col1:
        st.image('Images/richard.png',width=180)
    with col2:
        st.markdown('My expertise in surface science and in particular my research activities\
        related to understanding and controlling reactions in molecular ices induced by electrons, as well as reactions\
        at surfaces and interfaces induced by atomic species will help shed light on how complex molecules are formed in\
        ultra-cold interstellar space. The experiments will be performed using a Createc type LT-STM setup situated at the\
        Interdisciplinary Nanoscience Center (iNANO). ')
        st.markdown('[Google Scholar](https://scholar.google.com/citations?user=xSJAvTkAAAAJ&hl=en)')
        st.markdown('**Email**: <balog@phys.au.dk>')
    
    st.markdown('---')

    st.header('Postdoctoral Researchers')
    st.subheader('Dr. Kimberly Hsieh')
    col0,col1,col1a,col2=st.columns([1,4,1,22],gap="large")

    with col1:
        st.image('Images/kim.png',width=180)
    with col2:
        st.markdown('My research interest focusses in novel 2D materials and hybrids (such as topological insulator-superconductor hybrids)\
        using a combination of electronic transport and spectroscopy tools such as scanning probe microscopy ')
        st.markdown('[Google Scholar](https://scholar.google.com/citations?user=NxjhH_kAAAAJ&hl=en)')
        st.markdown('**Email**: <kimberly@phys.au.dk>')
        
    st.subheader('Dr. Subhadip Das')
    col0,col1,col1a,col2=st.columns([1,4,1,22],gap="large")

    with col1:
        st.image('Images/subha.png',width=180)
    with col2:
        st.markdown('My research interest in  magneto-Raman properties of two-dimensionals materials and their heterostrucures. ')
        st.markdown('[Google Scholar](https://scholar.google.co.in/citations?user=mZHHjxkAAAAJ&hl=en)')
        st.markdown('**Email**: <subhadipdas@phys.au.dk>')

    st.subheader('Dr. Lina Liu')    
    col0,col1,col1a,col2=st.columns([1,4,1,22],gap="large")

    with col1:
        st.image('Images/lina.png',width=180)
    with col2:
        st.markdown('My research interests focus on surface science studies of 2D materials and quantum systems, \
        including growth of 2D crystals, surface chemical and physical properties of topological materials and heterostructures. ')
        st.markdown('[Google Scholar](https://scholar.google.com.sg/citations?user=JD40TxMAAAAJ&hl=en)')
        st.markdown('**Email**: <lnliu@phys.au.dk>')

    st.markdown('---')
    st.header('Graduate Students')
    st.subheader('Kirstine Aggerbeck Stampe')
    col0,col1,col2=st.columns([1,4,19],gap="large")
    
    with col1:
        st.image('Images/blank.png',width=180)
    with col2:
        st.markdown('**Email**: <kas@phys.au.dk>')

    st.subheader('Ihsan Ahmed Kolasseri')
    col0,col1,col1a,col2=st.columns([1,4,1,22],gap="large")
    
    with col1:
        st.image('Images/ihsan.png',width=180)
    with col2:
        st.markdown('**Email**: <ihsanahmed@phys.au.dk>')    

    st.markdown('---')


    st.header('Visiting Researchers')
    st.subheader('Dr. Kim Khuong Huynh')
    col0,col1,col1a,col2=st.columns([1,4,1,22],gap="large")
    
    with col1:
        st.image('Images/kimk.png',width=180)
    with col2:
        st.markdown('Assistant Professor at Advanced Institute for Materials Research (AIMR), Tohoku University, Japan')
        st.markdown('[Google Scholar](https://scholar.google.com/citations?user=YnxKgoAAAAAJ&hl=en)')
        st.markdown('**Email**: <huynh.kim.khuong.b4@tohoku.ac.jp>')

        
    st.subheader('Dr. Yaping Qi')

        
    col0,col1,col1a,col2=st.columns([1,4,1,22],gap="large")
    
    with col1:
        st.image('Images/joyce.png',width=180)
    with col2:
        st.markdown('Macau University of Science and Technology, China')
        st.markdown('[Google Scholar](https://scholar.google.com/citations?user=qFJHjnEAAAAJ&hl=en)')
    


    

    



if selected=='Research Facilities':
    st.header('Interconnected Glovebox System with Inert Environment (< 1 ppm of O$_2$ and H$_2$O)')

   
 
    st.markdown('Our group has set up three interconnected glovebox systems (from Jacomex) capable of holding inert (N$_2$) atmosphere in either overpressure or\
    underpressure conditions with an autonomous purification unit continuously maintaining <1 ppm O$_2$ and H$_2$O under normal operating conditions. They allow (with purification\
    units off) intentionally introducing controlled amounts of gases (e.g. O$_2$, H$_2$O, CO$_2$) in the default N$_2$ atmosphere, creating various controlled-gas/exposure environment to\
    study material/surface chemical processes. The individual gloveboxes are designated and configured for 1) micromechanical exfoliation and stacking of 2D layered materials, 2)\
    characterization via optical spectroscopy techniques such as Fourier Transform Infrared (FTIR) spectroscopy and Raman and Photoluminescence (PL) spectroscopy, and 3) surface\
    probes such as atomic force microscopy and related techniques, respectively and described in more detail below. They are equipped with antechambers for the safe and efficient\
    transfer of air-sensitive samples between themselves,\
    without further exposure to ambient.  The valves between them allow each glovebox to be individually isolated and controlled with different environment when needed.  ')

    col0,col1,col2=st.columns([5,40,5],gap="large")
    with col1:
        st.image('Images/fig1.png')
    st.caption('Figure 1.  “Lab in Gloveboxes” – our 3 interconnected gloveboxes for 1) 2D material fabrication and transfer; 2) optical Raman and FTIR spectroscopy; and 3) \
    Atomic force microscopy (AFM) and other related scanning probe microscopies (SPM). ')

    st.subheader('Glovebox 1: Two-dimensional (2D) materials fabrication and transfer setup')
    with st.expander('Expand'):
        st.markdown('This glovebox contains a setup to perform scotch tape based micromechanical exfoliation of van der Waals (vdW) layered 2D materials. It has a motorized micromechanical\
    transfer setup (from HQ Graphene, Fig. 2a) equipped to stack layers in a wide variety of alignments and orientations. The substrate can be moved relative to the transparent stamp on\
    the mask holder in X-, Y- and Z-directions and also has rotational degree of freedom. This allows for accurate alignment of 2D crystal flakes during heterostructure fabrication that\
    can be used to create “Moire/twisted” structures with controlled twisting angle (which could tune material physical or even chemical properties that we intend to study later). The\
    substrate is held by vacuum and the temperature can be controlled between room temperature and 200 °C. Its compact design allows it to be placed inside a glovebox, allowing us to work\
    with air-sensitive 2D materials. The setup is equipped with a high-resolution microscope with long working distance objectives allowing for both bright field and dark field illuminations.\
    Fig. 2b shows an example of an \
    exfoliated/stacked monolayer h-BN/graphite/BN structure fabricated in this setup. ')

        col0,col1,col2=st.columns([5,20,5])
        with col1:
            st.image('Images/fig2.png')
        st.caption('Fig. 2. (a) Motorized transfer setup inside glovebox. (b) A heterostructure composed of monolayer (1L) boron nitride (BN), graphite, multilayer BN\
    (from top to bottom, as illustrated in the inset) on SiO$_2$/Si$^{++}$ wafer.')

    st.subheader('Glovebox 2: Optical (Raman and FTIR) Spectroscopy')
    with st.expander('Expand'):
        st.markdown('Raman and Fourier-transform infrared (FT-IR) spectroscopy are two widely used nondestructive analytical tools to study \
    vibrational properties down to micrometer scales of spatial resolution. As a vibrational mode can be either Raman or infrared active,\
    the two techniques are complementary and provide a complete picture of the photon-phonon interaction in the system. Notably, the vibrational\
    frequencies of each chemical bond are different and their spectral features act as a unique fingerprint for the compound. Importantly, any \
    chemical reaction and changes in structure can be systematically studied using these techniques. Additionally, information such\
    as bonding type, reaction rates and defects,and their evolution with external factors such as heating and laser irradiation can also be determined.')

        col0,col1,col2=st.columns([5,20,5],gap="large")
        with col1:
            st.image('Images/fig3.png')
        st.caption('Figure 3: (a) Picture of the Raman instrument showing two microscopes with scanning stage in all three directions. One of the stages resides\
    inside the glove-box for air-sensitive or controlled-environment measurements. (b) Data from the nearby glovebox shows the pressure (ΔP), oxygen and water contents\
    inside in parts per million (ppm) unit. (c) Three lasers for studying effects from different excitation energies. (d) Three Peltier cooled CCDs (labeled by 1, 2 and 3).\
    CCD1: 50 % enhanced quantum efficiency from 450 to 900 nm range. CCD2: Visible range detection. CCD3: InGaAs array detector for operating from 600 to 1700 nm range.\
    (e) Raman spectra previously measured in Chen lab in a single-layer graphene (on SiO2/Si) after various numbers of accumulated oxygen plasma exposure pulses, Ne.\
    The spectra are offset vertically for clarity.')
    
        st.markdown('Fig. 3(a) illustrates the Raman instrumental setup (Renishaw) with two different microscopes with spectral capabilities along and perpendicular to the\
    sample surface. Using a software feature called focus tracking, spatial mapping can also be done on uneven and curved surfaces. One of the confocal microscopes is for\
    ambient measurement and another one, placed beside the FTIR setup, is optically coupled with the spectrometer for air-sensitive/controlled environment measurement inside\
    the nitrogen glovebox (Jacomex), An example of the pressure, oxygen, and water content readout values of the glovebox is shown in Fig. 2(b). To examine samples with different\
    band gaps or excitation energy ranges, three excitation lasers of wavelengths 405nm, 532nm and 830nm (Fig. 3(c)) are available. The spectrometer consists of three switchable\
    gratings (1200, 1800 and 2400 lines per mm) and three thermoelectrically cooled charge-coupled device (CCDs) detectors (Fig. 3(d)) that are sensitive to visible and infrared\
    wavelength ranges. In addition to edge filters for high-frequency Raman measurements, a notch filter is available for 532 nm laser excitation for Stokes/Anti-Stokes\
    measurements, with a low energy filter to enable ultra-low frequency Raman measurements (∼ meV or <10 cm-1). As inter-layer vibrational modes can be detected in\
    this energy range, the instrument can determine layer number, changes in stacking configuration and inter-layer bonding strength. Also, linear and circular\
    polarization-resolved measurements can also be performed for all three lasers. Fig. 3e shows an exemplary previous study from PI’s group (measured in an earlier\
    Raman instrument), using systematic evolution of Raman spectra to monitor how graphene undergo chemical (e.g. oxidization) and structural (e.g. amorphorization,\
    vacancy generation) changes when it is subject to repeated O2 plasma exposure (commonly used as an etching tool).')

        col0,col1,col2=st.columns([5,20,5],gap="large")
        with col1:
            st.image('Images/fig4.png')
        st.caption('Figure 4: (a) FTIR setup (outside the glovebox) with joystick-controlled scanning stage in all three axes. (b) Optical micrograph of a multilayer hBN\
    flake and (c) its IR spectrum peak corresponding to the B-N bond stretching.')

        st.markdown('The FTIR instrument (Bruker corporation LUMOS) can measure the reflectivity, transmission and absorption spectra of 2D materials down to μm\
    level (Fig. 4(a)). The spectral range is from ∼ 1600 to 15000 nm, offering a versatile coverage of the infrared response spectrum for most materials. As \
    shown in Figs. 4(b) and (c), FTIR spectrum of hexagonal boron nitride (hBN) of few μm’s in size have been captured. The FTIR and Raman setups are currently\
    in the process of getting fully integrated inside the glove box. ')

    st.subheader('Glovebox 3: Atomic Force Microscope')
    with st.expander('Expand'):

        col0,col1,col2=st.columns([5,40,5],gap="large")
        with col1:
            st.image('Images/fig5.png')
            
        st.caption('Fig. 5. (a) Cypher S AFM inside glovebox with control unit adjacent to it. (b) Lateral force microscopy (LFM) image showing atomically resolved \
        lattice of highly oriented pyrolytic graphite (HOPG) obtained using Cypher S AFM.')
        st.markdown('In glovebox 3 we have an atomic force microscope (AFM) (Asylum Cypher S, Fig. 5a) which is a fast-scanning AFM compatible with a range of \
        scanning probe microscopy (SPM) modes and accessories. The standard operating modes available in our Cypher system are: ')
        st.markdown('**a. Contact mode AFM**: AFM imaging technique whereby the AFM tip tracks the topography of the sample by monitoring the cantilever deflection.  ')
        st.markdown('**b. Tapping mode (AC mode)**: The cantilever is typically oscillated mechanically by a small piezo electric actuator and the drive frequency \
        is swept to locate the first resonance of the cantilever. The drive frequency is then set at or near that resonance frequency. The optical \
        detector senses the oscillatory motion of the cantilever and the electronics inside the controller measure the amplitude and phase of this oscillation with\
        respect to the drive signal. ')
    
        st.markdown('**c. Electrostatic Force Microscopy (EFM)**: EFM provides information on the local electrostatic forces between the tip and the sample which leads\
        to a shift in the phase lag of the mechanically driven cantilever. ')
        st.markdown('**d. Scanning Kelvin Probe Force Microscopy (KPFM)**: Scanning Kelvin Probe Microscopy (SKPM) is a technique that detects the potential difference\
        between the probe tip and the sample. ')
        st.markdown('**e. Lateral Force Mode (LFM)**: A specialized mode of Contact Mode AFM, LFM can tell how much the cantilever twists from the friction experienced by the\
        tip during scanning. This signal is measured by the same quadrant photodetector that measures the cantilever deflection, except that “left” and “right” halves of the\
        photodetector are subtracted to give the lateral deflection (twist) of the cantilever.\
        Fig. 5b shows an example of atom-resolved lattice image of graphite measured with LFM using our Cypher AFM. We have also obtained atomic lattice images on h-BN.')
        st.markdown('**f. Piezoresponse Force Microscopy (PFM)**: PFM measures the mechanical response when an electrical voltage is applied to the sample surface with \
        a conductive AFM tip. The sample deforms in response to the applied voltage, \
        which in turn, causes the cantilever to deflect, which can then be measured and interpreted in terms of the piezoelectric properties of the sample. ')

        st.markdown('**g. Conductive AFM (CAFM) with ORCA™**: Conductive AFM or CAFM provides a map of the local conductivity of a sample at a fixed bias.')
        st.markdown('**h. High voltage PFM**: The high voltage PFM option allows users to conduct PFM measurements at high biases of up to ±150 V. ')

        st.markdown('	It is well known that AFM-based methods are widely used to measure the mechanical properties of materials but additionally, advanced \
     AFMs such as our Cypher AFM have specialized modes which can be harnessed in the study of various chemical properties, catalytic and functionalization reactions\
     on the surface of materials. For example, people have studied catalytic processes using in-situ AFM imaging down to single-molecule resolution. They observed\
     spontaneous formation of methanol–water structures on the surface of highly oriented pyrolytic graphene (HOPG), with the catalysis rate enhanced by electric fields.\
     Meanwhile, another group used high-resolution AFM imaging to monitor the self-assembly dynamics of 1D peptide crystals on the surface of MoS$_2$ and observed 2D arrays\
     growing one row at a time, a result in line with the principles of classical nucleation theory. \
     AFM can also be used to study rate of etching reactions such as that of silicon (Si) by plasmas containing different percentages of sulfur hexafluoride (SF$_6$).')

        
    st.header('Scanning Tunneling Microscope (STM)')
    
    st.markdown('STM has played a crucial role in the research field of surface science and condensed matter. The STM system recently commissioned in our lab (Figure 6a)\
    is a state-of-art ultra-high-vacuum (UHV) low temperature scanning tunneling microscope (LT-STM) (from Unisoku) allowing imaging, manipulation and tunnelling spectroscopy\
    at the atomic level. It provides great opportunities for in-situ studies of on-surface reactions, as well as the underlying physics. Our newly installed Unisoku STM system\
    is equipped with a few world’s most advanced capabilities for studying reactions. The system has several separate chambers (preparation chamber and exchange chamber, which\
    is further equipped with a stage that can cool down the sample with liquid helium) that can be routinely connected to a variety of gas lines, such as H$_2$O, O$_2$, H$_2$, CO or\
    CO$_2$ providing means for well controlled reaction studies with individual or mixture of gases, before the sample is transferred to STM for in-depth atomic-level studies.\
    Atomic C, H and O crackers are available for studies involving reactions induced by radicals which may include controlled generation of defects at surfaces or synthesis\
    of larger molecules. Finally, the attached metal and molecular evaporators allow us to investigate the growth of epitaxial layers but also to study e.g. molecular\
    self-assembly as a function of surface temperature and the type of the surface. Controlled deposition down to 20K is possible. Further specific features of the system include: ')
    col0,col1,col2=st.columns([10,60,10],gap="large")
    with col1:
        st.image('Images/fig6.png')
    st.caption('Figure 6. (a) Unisoku LT-STM recently installed and commissioned in PI’s new lab in Aarhus.  Relevant examples from previous studies: \
    (b) STM (lower) and ARPES (upper) data of CVD graphene grown on Ir(111) surface  before (left) and after (right) surface-assisted hydrogenation. \
    The STM data show topographic image while the ARPES data show band structure of graphene around the Dirac point. \
    (c) Atomic-resolution STM images of monolayer PdTe2 and patterned PtTe2, formed after tellurization reactions of single crystal Pd and Pt surfaces. ')

    st.subheader('Ultra-low temperature and high magnetic field')

    st.markdown('The STM system can be operated down to temperature of 300 mK and up to a magnetic field of 16 T (perpendicular to sample surface). \
    The ultra-low temperature, together with the atomic-resolution microscopy and spectroscopy provides an excellent platform for studies of a variety of\
    inter-molecular reactions, in particular on weakly bound surfaces such as graphite or graphene. Additionally, one can determine preferential adsorption sites; \
    image the orientation of the molecule on the surface; follow the diffusion on the surface; image molecular orbitals and consequently induce particular reaction\
    by injecting the tunnelling electrons into the specific orbital to study site-selective chemistry. The state-of-the-art in STM induced reactions include both\
    the site selective bond rupture as well as synthesis of a new molecule via bond formation.  On the other hand, the capability of applying high magnetic \
    field opens opportunities for new type of selective reactions, such as magnetic field induced ordering of magnetic molecules,\
    synthesis of larger molecules from the individual magnetic constituents, and novel synthesis controlled by magnetic fields or on magnetic substrates. ')

    st.subheader('Study of cleaved air-sensitive samples')
    st.markdown('The STM system contains a sample preparation chamber with a base pressure at 10-10 mbar, which is important for the air sensitive samples.\
    The chamber can also be connected with various gas lines to intentionally induce chemical reactions to the sample if needed. For samples that cannot be \
    cleaned by standard Ar+ sputter/anneal cycles, the system is equipped with a cleaving stage allowing us to break the sample in UHV and thus obtain a clean\
    pristine surface. Sample cleavage is also possible at temperatures down to 20K as for some materials the\
    cleaved surface may undergo phase transition at room temperature (RT) or may become rapidly contaminated due to the high reactivity at RT. ')

if selected=='Openings':
    st.markdown('Prof. Yong P. Chen from Purdue University has received a Villum Investigator Grant\
    (<https://phys.au.dk/en/news/item/artikel/from-usa-to-aarhus-with-hybrid-quantum-materials/>) to establish a new lab on Quantum Materials and Measurements \
    (co-managed by Assistant Prof. Richard Balog) and Center on Hybrid Quantum Materials and Devices at Aarhus University, Denmark.')

    st.markdown('Research interests of the new lab and Center include:')

    st.markdown('1) Fabrication and studies of 2D, topological and hybrid quantum materials, structures and devices with novel physical and chemical properties,\
    and potential relevance in quantum information (e.g. computing or sensing) applications;')

    st.markdown('2) Multi-modal and in-operando measurements (esp. at low temperatures and/or high magnetic fields) of such materials and devices based on or combining \
    electronic transport, optical, scanning probe microscopy and quantum sensing techniques.') 

    st.markdown('Perspective students and postdocs interested in research opportunities in Chen-Balog lab and Villum Center for Hybrid Quantum Materials and Devices are welcome\
    to contact <yongchen@phys.au.dk> (Yong) and <balog@phys.au.dk> (Richard)')

    st.markdown('A representative PhD project recently announced: "Studies of quantum emitters and single photon sources in layered 2D materials by STM-induced luminescence"')
    
if selected=='Gallery':
    col0,col1,col2=st.columns([10,40,10],gap="large")
    with col1:
        st.image('Images/Gallery/1 (4).jpg', caption='Optical microscope and Wirebonding setup')
        st.image('Images/Gallery/1 (5).jpg', caption='Fume hood for chemical processing and spin coating. ')
        st.image('Images/Gallery/1 (6).jpg', caption='Raman spectrum being acquired by the Renishaw WiRE software.')
        st.image('Images/Gallery/1 (7).jpg', caption='Graphene is being picked up using the transfer stage')
        st.image('Images/Gallery/1 (8).jpg', caption='Graphite-hBN heterostructure')
        st.image('Images/Gallery/1 (9).jpg', caption='12 Tesla magnet from ICEOxford being assembled')
        st.image('Images/Gallery/1 (10).jpg', caption='Vibrational isolation stage is being set up for scanning probes by Nanomagnetics Inc.')
        st.image('Images/Gallery/1 (12).jpg', caption='Three probes for AC, DC, and scanning Hall measurements')
        st.image('Images/Gallery/1 (13).jpg', caption='Device inside the chip carrier that can rotate along both theta and phi axes.')
        st.image('Images/Gallery/1 (14).jpg', caption='Dinner with collaborators')


        
        







