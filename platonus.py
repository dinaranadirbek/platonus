
агм_бағасы = []
модуль1_бағасы = []
модуль2_бағасы = []
сессия_бағасы = []


print("Агм бағаларын енгізіңіз :")
агм_бағасы = list(map(int, input().split()))


print("1-ші модуль бағаларын енгізіңіз :")
модуль1_бағасы = list(map(int, input().split()))


print("2-ші модуль бағаларын енгізіңіз :")
модуль2_бағасы = list(map(int, input().split()))


print("Сессия бағаларын енгізіңіз :")
сессия_бағасы = list(map(int, input().split()))


W_A = 0.3  # Агм
W_1 = 0.3  # 1-ші модуль
W_2 = 0.2  # 2-ші модуль
W_S = 0.2  # Сессия


орташа_агм = sum(агм_бағасы) / len(агм_бағасы)
орташа_модуль1 = sum(модуль1_бағасы) / len(модуль1_бағасы)
орташа_модуль2 = sum(модуль2_бағасы) / len(модуль2_бағасы)
орташа_сессия = sum(сессия_бағасы) / len(сессия_бағасы)


қорытынды_баға = (орташа_агм * W_A) + (орташа_модуль1 * W_1) + (орташа_модуль2 * W_2) + (орташа_сессия * W_S)


print(f"Студенттің қорытынды бағасы: {қорытынды_баға:.2f}")
