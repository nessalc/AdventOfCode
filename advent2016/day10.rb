f=File.open(ARGV[0])
lines=f.readlines().compact
$botlist=Array.new(210)
$outputbin=[]
class Bot
  @lowloc,@low,@highloc,@high='',nil,'',nil
  def initialize(id,instructions=['',nil,'',nil],chips=[])
    @id=id
    @lowloc,@low,@highloc,@high=instructions
    @chips=chips
    if @chips.length==2 and instructions.all?
      act()
    end
  end
  def add_instructions(instructions)
    @lowloc,@low,@highloc,@high=instructions
    if @chips.length==2
      act()
    end
  end
  attr_accessor :chips
  attr_accessor :id
  def add_chip(value)
    @chips<<value
    if @chips.length==2 and [@lowloc,@low,@highloc,@high].all?
      act()
    elsif @chips.length>2
      print_bot()
    end
  end
  def act()
    l,h=@chips.sort
    if l==17 and h==61
      puts "Part 1: Bot ##{@id}"
    end
    if @lowloc=='bot'
      if !$botlist[@low]
        $botlist[@low]=Bot.new(@low)
      end
      $botlist[@low].add_chip(l)
    else
      if $outputbin[@low]
        $outputbin[@low]<<l
      else
        $outputbin[@low]=l
      end
    end
    if @highloc=='bot'
      if !$botlist[@high]
        $botlist[@high]=Bot.new(@high)
      end
      $botlist[@high].add_chip(h)
    else
      if $outputbin[@high]
        $outputbin[@high]<<h
      else
        $outputbin[@high]=h
      end
    end
    @chips.clear
  end
  def print_bot()
    puts "Bot #{@id} (chips #{@chips}): low goes to #{@lowloc} #{@low}, high goes to #{@highloc} #{@high}"
  end
end
#$botlist[1]=Bot.new(1,['',nil,'',nil],[3])
#$botlist[2]=Bot.new(2,['',nil,'',nil],[2,5])
while lines.length>0
  line=lines.shift
  case line.split()[0].strip
  when "value"
    value,bot=line.match(/(\d+).*?(\d+)/)[1,2].map { |t| t.to_i }
    if !$botlist[bot]
      $botlist[bot]=Bot.new(bot)
    end
    if $botlist[bot].chips.length==2
      lines.push(line)
    else
      $botlist[bot].add_chip(value)
    end
  when "bot"
    bot,low,high=line.match(/(\d+).*?(\d+).*?(\d+)/)[1,3].map { |t| t.to_i }
    lowloc,highloc=line.match(/\d+.*(bot|output)\s\d+.*(bot|output)\s\d+/)[1,2]
    if $botlist[bot]
      $botlist[bot].add_instructions([lowloc,low,highloc,high])
    else
      $botlist[bot]=Bot.new(bot,[lowloc,low,highloc,high])
    end
  end
end
puts "Part 2: #{$outputbin[0,3]}=#{$outputbin[0,3].reduce(:*)}"
