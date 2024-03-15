randint = lambda start,stop: exec('''globals()["_l"] = float(f'0.{abs(hash(str(globals().get("_l") or hash(id))))}')''') or int(_l*(stop-start+1))+start
