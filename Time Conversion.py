def timeConversion(s):
    if s[-2:] == 'AM':
      if s[0:2] == '12':
        tc_result = str(s.replace('12', '00', 1))
      else : tc_result = s
    if s[-2:] == 'PM' :
      if s[0:2] != '12':
        tc_result = str(int(s[0:2])+12)+s[2:]
      else : tc_result = s
    return tc_result[:8]
