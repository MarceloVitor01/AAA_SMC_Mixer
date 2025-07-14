# EncoderComponent.py (Versão Corrigida para Ableton Live 11/12)
from _Framework.ControlSurfaceComponent import ControlSurfaceComponent
from _Framework.ButtonElement import ButtonElement


class EncoderComponent(ControlSurfaceComponent):
    """
    Componente que transforma um knob (que envia um CC absoluto) em dois
    'botões' virtuais, um para o movimento de subida (direita) e outro para
    o de descida (esquerda).
    """

    def __init__(self, *a, **k):
        super(EncoderComponent, self).__init__(*a, **k)

        self._control = None
        self._last_value = -1

        # --- CORREÇÃO APLICADA AQUI ---
        # Adicionamos um quarto argumento (o 'identifier') para ser compatível
        # com versões mais recentes da API do Ableton. Usamos números que
        # provavelmente não entrarão em conflito com nada (126 e 127).
        self._up_button = ButtonElement(True, 0, 0, identifier=127)
        self._down_button = ButtonElement(True, 0, 0, identifier=126)
        # --- FIM DA CORREÇÃO ---

    def disconnect(self):
        if self._control:
            self._control.remove_value_listener(self._on_value_changed)
        super(EncoderComponent, self).disconnect()
        self._up_button = None
        self._down_button = None
        self._control = None

    def set_control(self, control):
        if self._control:
            self._control.remove_value_listener(self._on_value_changed)
        self._control = control
        if self._control:
            self._control.add_value_listener(self._on_value_changed)

    def up_button(self):
        return self._up_button

    def down_button(self):
        return self._down_button

    def _on_value_changed(self, value):
        if self._last_value == -1:
            self._last_value = value
            return

        if value > self._last_value:
            self._up_button.receive_value(127)
            self._up_button.receive_value(0)
        elif value < self._last_value:
            self._down_button.receive_value(127)
            self._down_button.receive_value(0)

        self._last_value = value
