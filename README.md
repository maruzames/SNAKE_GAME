Criação do Jogo da Cobrinha, 
Aula pelo YouTube.

USANDO a biblioteca PYGAME

1. configurações iniciais

	cores, tamanho de tela, velocidade de jogo

2. loop infinito 

	def running_game():
	    fimdejogo = False

    	while not fimdejogo:

        	for evento in pygame.event.get():
            	if evento.type == pygame.QUIT:
                	fimdejogo = True

3. desenhar os objetos do jogo

4. criar a logica de terminação do jogo

5. pegar as interações do usuário 