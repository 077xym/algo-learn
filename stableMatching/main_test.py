from stableMatching.main import stable_match

vic_list = ["Ber", "Amy", "Dia", "Eri", "Cla"]
wya_list = ["Dia", "Ber", "Amy", "Cla", "Eri"]
Xav_list = ["Ber", "Eri", "Cla", "Dia", "Amy"]
Yan_list = ["Amy", "Dia", "Cla", "Ber", "Eri"]
Zeus_list = ["Ber", "Dia", "Amy", "Eri", "Cla"]

man_preference = {"Vic": vic_list, "Wya": wya_list, "Xav": Xav_list,
                  "Yan": Yan_list, "Zeus": Zeus_list}

amy_list = ["Zeus", "Vic", "Wya", "Yan", "Xav"]
ber_list = ["Xav", "Wya", "Yan", "Vic", "Zeus"]
cla_list = ["Wya", "Xav", "Yan", "Zeus", "Vic"]
dia_list = ["Vic", "Zeus", "Yan", "Xav", "Wya"]
eri_list = ["Yan", "Wya", "Zeus", "Xav", "Vic"]

woman_preference = {"Amy": amy_list, "Ber": ber_list, "Cla": cla_list,
                    "Dia": dia_list, "Eri": eri_list}


if __name__ == "__main__":
    print(stable_match(man_preference, woman_preference))
