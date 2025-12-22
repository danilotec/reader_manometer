def angle_to_percent(angle: float) -> float:
    '''
    :param angle: esse paramentro deve ser preenchido com o retorno do metodo get_angle da classe manometer
    :type angle: float
    
    :return: retorna o angulo do ponteiro do manometro
    :rtype: float
    '''

    if angle < 135:
        angle += 360

    percentual = (angle - 135) / 270
    return max(0.0, min(1.0, percentual))

def get_volume(percent: float, scale: float) -> float:
    '''    
    :param percent: se refere a porcentagem do circulo do manometro
    esse valor deve vir da função angle_to_percent 
    :type percent: float
    
    :param scale: se refere ao valor maximo de leitura do manometro, que reprezenta o 100%
    do mesmo
    :type scale: float
    
    :return: retorna o valor real do manometro baseado na posição do ponteiro
    :rtype: float
    '''
    return percent * scale