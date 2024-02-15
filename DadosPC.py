import psutil

def onbter_informacoes_memoria():
    memoria_fisica = psutil.virtual_memory()

    print('Informações de Memória Física:')
    print(f'Total: {memoria_fisica.total} bytes')
    print(f'Disponível: {memoria_fisica.available} bytes')
    print(f'Usado: {memoria_fisica.used} bytes')
    print(f'Percentagem de Uso: {memoria_fisica.percent}%')

    memoria_swap = psutil.swap_memory()
    print('\nInfomações de Memória de Swap:')
    print(f'Total: {memoria_swap.total} bytes')
    print(f'Disponível: {memoria_swap.free} bytes')
    print(f'Usado: {memoria_swap.used} bytes')
    print(f'Percentagem de Uso: {memoria_swap.percent}%')

if __name__ == "__main__":
    onbter_informacoes_memoria()
    
