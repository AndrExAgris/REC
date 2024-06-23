from mininet.topo import Topo

class Topologia(Topo):

    def __init__(self):
        #Inicia a topologia da rede
        Topo.__init__( self )

        # Hosts
        pc0 = self.addHost('PC0')
        pc1 = self.addHost('PC1')
        pc2 = self.addHost('PC2')
        pc3 = self.addHost('PC3')
        pc4 = self.addHost('PC4')
        pc5 = self.addHost('PC5')
        pc6 = self.addHost('PC6')
        pc7 = self.addHost('PC7')
        pc8 = self.addHost('PC8')
        pc9 = self.addHost('PC9')

        # Switches
        sw0 = self.addSwitch('SW0', failMode='standalone', stp=True)
        sw1 = self.addSwitch('SW1', failMode='standalone', stp=True)
        sw2 = self.addSwitch('SW2', failMode='standalone', stp=True)
        sw3 = self.addSwitch('SW3', failMode='standalone', stp=True)
        sw4 = self.addSwitch('SW4', failMode='standalone', stp=True)
        sw5 = self.addSwitch('SW5', failMode='standalone', stp=True)
        sw6 = self.addSwitch('SW6', failMode='standalone', stp=True)

        # Links
        self.addLink(pc0, sw1)
        self.addLink(pc1, sw1)
        self.addLink(pc2, sw3)
        self.addLink(pc3, sw3)
        self.addLink(pc4, sw4)
        self.addLink(pc5, sw4)
        self.addLink(pc6, sw5)
        self.addLink(pc7, sw5)
        self.addLink(pc8, sw2)
        self.addLink(pc9, sw2)

        self.addLink(sw0, sw1)
        self.addLink(sw0, sw3)
        self.addLink(sw0, sw4)
        self.addLink(sw0, sw5)
        self.addLink(sw0, sw6)
        self.addLink(sw1, sw6)
        self.addLink(sw2, sw6)

topos = { 'Topologia': ( lambda: Topologia() ) }