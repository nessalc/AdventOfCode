f=File.open(ARGV[0])
program=f.readlines().map { |line| line.strip }
def run_program(program,a=0,b=0,c=0,d=0)
  counter=0
  counter_max=program.length
  while counter<counter_max
    instruction=program[counter].split
    case instruction[0]
    when 'cpy'
      begin
        eval instruction[2]+'='+instruction[1]
      end
    when 'inc'
      eval instruction[1]+'+=1'
    when 'dec'
      eval instruction[1]+'-=1'
    when 'jnz'
      test=eval instruction[1]+'!=0'
      if test
        counter+=(eval instruction[2])-1 #-1 to offset counter increment at end of loop
      end
    when 'tgl'
      begin
        newinst=program[counter+(eval instruction[1])].split
      rescue
        counter+=1
        next
      end
      case newinst[0]
      when 'inc'
        program[counter+(eval instruction[1])]=['dec',newinst[1]].join(' ')
      when 'jnz'
        program[counter+(eval instruction[1])]=['cpy',newinst[1,2]].join(' ')
      when 'dec'
        program[counter+(eval instruction[1])]=['inc',newinst[1]].join(' ')
      when 'cpy'
        program[counter+(eval instruction[1])]=['jnz',newinst[1,2]].join(' ')
      when 'tgl'
        program[counter+(eval instruction[1])]=['inc',newinst[1]].join(' ')
      end
    end
    counter+=1
  end
  return a,b,c,d
end
a,b,c,d=run_program(program,7)
puts "Part 1: Register a = #{a}"
a,b,c,d=run_program(program,12)
puts "Part 2: Register a = #{a}"
