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


speed_up_dez_k_random = [1.259675838, 0.5831593187, 0.6297461446, 0.4368355327,
                         0.3275674398, 0.2603234883, 0.1398314349, 0.04891282186]

speed_up_cem_k_random = [1.385679903, 1.341919775, 1.318274344, 1.284057334,
                         1.09126444, 0.9878733663, 0.6967919539, 0.4168986933]

speed_up_um_mi_random = [1.451300188, 1.129436078, 1.761612358, 1.925805396,
                         2.197207094, 2.222580419, 2.305211845, 1.822317215]

speed_up_dez_mi_random = [1.440039223, 1.562519098, 1.605509843, 1.622765016,
                          1.650691192, 1.732601661, 1.788014142, 1.876947617,
                          1.916686226, 1.910915472, 1.895846484]


speed_up_dez_k_inverso = [1.097461922, 0.5498355862, 0.4042566846, 0.4137015265,
                          0.2236822886, 0.1986656887, 0.1119502215, 0.05756217593]

speed_up_cem_k_inverso = [1.469822523, 1.065964425, 1.104549525, 1.069622476,
                          0.888937316, 0.805485141, 0.626201909, 0.399518577]

speed_up_um_mi_inverso = [1.376069944, 1.434748004, 1.214730335, 1.145662343,
                          1.178180105, 1.012953795, 0.928949486, 1.017083731]

speed_up_dez_mi_inverso = [1.512691278, 1.766498178, 1.877694623, 1.928606359,
                           1.911499078, 1.935727208, 2.024871552, 2.003810540,
                           1.966633943, 1.844867890, 1.647829039]

import matplotlib.pyplot as plt
import numpy as np

threads = [2,4,8,16,32,64,128, 256]
#plt.yticks(speed_up_dez_k_random)
#plt.xlim(128)
#plt.plot(threads, speed_up_dez_k_random)
t = ["Thread 2", "Thread 4", "Thread 8", "Thread 16","Thread 32", "Thread 64", "Thread 128", "Thread 256"]
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
#lt.plot(t2, speed_up_dez_mi_random, "o-", label = "10mi Inteiros")
#plt.legend(bbox_to_anchor=(0.80, 0.75), loc=2, borderaxespad=0.)

plt.title("Entrada Inversa")
#plt.plot(t, speed_up_dez_k_inverso, "s-", label="10k Inteiros")
#plt.plot(t, speed_up_cem_k_inverso, "D-", label="100k Inteiros")
#plt.plot(t, speed_up_um_mi_inverso, "p-", label = "1mi Inteiros")
plt.plot(t2, speed_up_dez_mi_inverso, "o-", label = "10mi Inteiros")
plt.legend(bbox_to_anchor=(0.80, 0.95), loc=2, borderaxespad=0.)

plt.show()

