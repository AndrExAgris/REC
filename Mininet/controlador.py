from ryu.app.simple_switch import SimpleSwitch
from ryu.controller import Controller
from ryu.ofproto import ofproto_v1_3


class MeuControlador(Controller):

    def __init__(self, **kwargs):
        super(MeuControlador, self).__init__(**kwargs)
        self.mac_to_port = {}

    def feature_request_handler(self, req):
        self.send_feature_reply(req, req.feature_request.ofp_version)

    def packet_in_handler(self, msg):
        datapath = msg.datapath
        ofproto = datapath.ofproto
        pkt = Packet(msg.data)

        # Extrair MAC de destino e origem
        dst_mac = pkt.get_dst_mac()
        src_mac = pkt.get_src_mac()

        # Verifique se o MAC de destino está no dicionário mac_to_port
        if dst_mac in self.mac_to_port:
            # Se o MAC de destino estiver no dicionário, obtenha a porta de saída
            out_port = self.mac_to_port[dst_mac]

            # Crie uma ação de envio para a porta de saída
            actions = [ofproto.ofproto13.OFPActionOutput(out_port)]

            # Envie o pacote para o switch com as ações
            data = self.send_packet_out(datapath, msg.buffer_id, pkt, actions)
        else:
            # Se o MAC de destino não estiver no dicionário, inunde o pacote para todas as portas, exceto a porta de entrada
            in_port = msg.in_port
            actions = [ofproto.ofproto13.OFPActionOutput(port) for port in datapath.ofproto.ports
                       if port != in_port]
            data = self.send_packet_out(datapath, msg.buffer_id, pkt, actions)

        # Atualize o dicionário mac_to_port com as informações do pacote
        self.mac_to_port[src_mac] = msg.in_port


if __name__ == '__main__':
    controlador = MeuControlador()
    controlador.run()