f=File.open(ARGV[0])
lines=f.readlines()
lines.map! { |line| line.strip.chars }
lines.transpose.each do |line|
  n=0
  max=0
  line.uniq.each do |c|
    line.count(c)
