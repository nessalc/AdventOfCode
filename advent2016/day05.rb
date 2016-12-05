require 'digest'
f=File.open(ARGV[0])
lines=f.readlines()
input=lines[0].strip
md5=Digest::MD5.new
password1=''
num='0'
while password1.length<8
  d=md5.hexdigest(input+num)
  if d[0,5]=='00000'
    password1+=d[5]
    puts password1
  end
  num.succ!
end
puts "Part 1: Password is #{password1}"
password2='_'*8
num='0'
prev=''
done=0
while done<8
  d=md5.hexdigest(input+num)
  if d[0,5]=='00000' and '01234567'.include?(d[5]) and (not prev.include?(d[5]))
    password2[d[5].to_i]=d[6]
    prev+=d[5]
    puts password2
    done+=1
  end
  num.succ!
end
puts "Part 2: Password is #{password2}"
