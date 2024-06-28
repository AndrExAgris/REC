from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel

class Topologia(Topo):
    def __init__(self):
        Topo.__init__(self)

        # Hosts
        PC0 = net.addHost('PC0', ip='127.0.0.2')
        PC1 = net.addHost('PC1', ip='127.0.0.3')
        PC2 = net.addHost('PC2', ip='127.0.0.4')
        PC3 = net.addHost('PC3', ip='127.0.0.5')
        PC4 = net.addHost('PC4', ip='127.0.0.6')
        PC5 = net.addHost('PC5', ip='127.0.0.7')
        PC6 = net.addHost('PC6', ip='127.0.0.8')
        PC7 = net.addHost('PC7', ip='127.0.0.9')
        PC8 = net.addHost('PC8', ip='127.0.0.10')
        PC9 = net.addHost('PC9', ip='127.0.0.11')

        # Switches
        sw0 = self.addSwitch('SW0')
        sw1 = self.addSwitch('SW1')
        sw2 = self.addSwitch('SW2')
        sw3 = self.addSwitch('SW3')
        sw4 = self.addSwitch('SW4')
        sw5 = self.addSwitch('SW5')
        sw6 = self.addSwitch('SW6')

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

def run():
    topo = Topologia()
    net = Mininet(topo=topo, switch=OVSSwitch, build=False)
    net.build()

    # Configurar switches no modo standalone e ativar STP
    for sw in net.switches:
        sw.cmd('ovs-vsctl set Bridge', sw, 'stp_enable=true')
        sw.cmd('ovs-vsctl set-fail-mode', sw, 'standalone')

    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()

