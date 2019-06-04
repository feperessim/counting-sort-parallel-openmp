def show_results(speed_up_list):
    exp = 2
    threads = 2
    for speed_up in speed_up_list:
        print(threads, " Threads - ", speed_up)
        threads = 2**exp
        exp += 1
    print()


dez_k_random_serial =  0.0003969
cem_k_random_serial = 0.003585
um_mi_random_serial = 0.157828
dez_mi_random_serial = 2.26162

dez_k_random_parallel_threads = [0.000979748,
                                 0.000337674,
                                 0.000374396,
                                 0.000629315,
                                 0.00136845,
                                 0.00225381,
                                 0.00400966]
speed_up_dez_k_random = [dez_k_random_serial/value for value in dez_k_random_parallel_threads]

cem_k_random_parallel_threads = [0.00304282,
                                 0.00232517,
                                 0.00442855,
                                 0.00386329,
                                 0.00407322,
                                 0.00466986,
                                 0.00763041]
speed_up_cem_k_random = [cem_k_random_serial/value for value in cem_k_random_parallel_threads]

um_mi_random_parallel_threads = [0.105916,
                                 0.109693,
                                 0.0832931,
                                 0.0870843,
                                 0.0803605,
                                 0.0797436,
                                 0.0800263]
speed_up_um_mi_random = [um_mi_random_serial/value for value in um_mi_random_parallel_threads]

dez_mi_random_parallel_threads = [1.68322,
                                 1.54582,
                                 1.52636,
                                 1.52665,
                                 1.50517,
                                 1.45658,
                                 1.40277,
                                 1.38402,
                                 1.33204,
                                 1.29833,
                                 1.36189]
speed_up_dez_mi_random = [dez_mi_random_serial/value for value in dez_mi_random_parallel_threads]

print("Speed-up de números aleatórios\n")

print("Speed up - 10.000 Inteiros")
show_results(speed_up_dez_k_random)

print("Speed up - 100.000 Inteiros")
show_results(speed_up_cem_k_random)

print("Speed up - 1.000.000 Inteiros")
show_results(speed_up_um_mi_random)

print("Speed up - 10.000.000 Inteiros")
show_results(speed_up_dez_mi_random)

dez_k_inverso_serial = 0.0002459
cem_k_inverso_serial = 0.0032409
um_mi_inverso_serial = 0.03418
dez_mi_inverso_serial = 0.314927

dez_k_inverso_parallel_threads = [0.000226299,
                                 0.000280118,
                                 0.000578102,
                                 0.00047348,
                                 0.000780068,
                                 0.00256494,
                                 0.00340071]
speed_up_dez_k_inverso = [dez_k_inverso_serial/value for value in dez_k_inverso_parallel_threads]

cem_k_inverso_parallel_threads = [0.00407513,
                                 0.00401855,
                                 0.00288539,
                                 0.00342148,
                                 0.00364228,
                                 0.00510353,
                                 0.00662513]
speed_up_cem_k_inverso = [cem_k_inverso_serial/value for value in cem_k_inverso_parallel_threads]


um_mi_inverso_parallel_threads = [0.023367,
                                 0.0252511,
                                 0.0298664,
                                 0.0275129,
                                 0.031698,
                                 0.0316726,
                                 0.0309517]
speed_up_um_mi_inverso = [um_mi_inverso_serial/value for value in um_mi_inverso_parallel_threads]


dez_mi_inverso_parallel_threads = [0.27633,
                                 0.263342,
                                 0.246083,
                                 0.229895,
                                 0.239692,
                                 0.231531 ,
                                 0.213705,
                                 0.221459,
                                 0.226786,
                                 0.287156,
                                 0.285621]
                                   
speed_up_dez_mi_inverso = [dez_mi_inverso_serial/value for value in dez_mi_inverso_parallel_threads]

print("Speed-up - Inteiros com ordenação inversa\n")

print("Speed up - 10.000 Inteiros")
show_results(speed_up_dez_k_inverso)

print("Speed up - 100.000 Inteiros")
show_results(speed_up_cem_k_inverso)

print("Speed up - 1.000.000 Inteiros")
show_results(speed_up_um_mi_inverso)

print("Speed up - 10.000.000 Inteiros")
show_results(speed_up_dez_mi_inverso)


import matplotlib.pyplot as plt
import numpy as np

threads = [2,4,8,16,32,64,128]
#plt.yticks(speed_up_dez_k_random)
#plt.xlim(128)
#plt.plot(threads, speed_up_dez_k_random)
t = ["Thread 2", "Thread 4", "Thread 8", "Thread 16","Thread 32", "Thread 64", "Thread 128"]
t2 = ["Thread 2", "Thread 4", "Thread 8", "Thread 16","Thread 32", "Thread 64", "Thread 128",
      "Thread 256", "Thread 512", "Thread 1024", "Thread 2048"]
#plt.xticks(threads, t)
# Rotaciona os valores do eixo X
plt.xticks(rotation=25)
plt.ylabel("Speedup", fontsize=14, labelpad=15)
# Coloca linhas horizontais
plt.gca().yaxis.grid(True)
#Tira a caixa ao entorno do gráfico
plt.box(False)
#plt.title("Entrada Aleatória")
#plt.plot(t, speed_up_dez_k_random, "s-", label="10k Inteiros")
#plt.plot(t, speed_up_cem_k_random, "D-", label="100k Inteiros")
#plt.plot(t, speed_up_um_mi_random, "p-", label = "1mi Inteiros")
#plt.plot(t2, speed_up_dez_mi_random, "o-", label = "10mi Inteiros")
#plt.legend(bbox_to_anchor=(0.80, 0.75), loc=2, borderaxespad=0.)

plt.title("Entrada Inversa")
#plt.plot(t, speed_up_dez_k_inverso, "s-", label="10k Inteiros")
#plt.plot(t, speed_up_cem_k_inverso, "D-", label="100k Inteiros")
#plt.plot(t, speed_up_um_mi_inverso, "p-", label = "1mi Inteiros")
plt.plot(t2, speed_up_dez_mi_inverso, "o-", label = "10mi Inteiros")
plt.legend(bbox_to_anchor=(0.80, 0.75), loc=2, borderaxespad=0.)

plt.show()

