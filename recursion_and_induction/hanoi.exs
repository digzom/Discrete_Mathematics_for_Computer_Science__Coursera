defmodule HanoiTower do
  def steps_to_solve_for(1, from, to), do: IO.puts("Move from #{from} to #{to}")

  def steps_to_solve_for(n, from, to) do
    unused_rod = 6 - from - to

    steps_to_solve_for(n - 1, from, unused_rod)
    IO.puts("Move from #{from} to #{to}")
    steps_to_solve_for(n - 1, unused_rod, to)
  end
end

HanoiTower.steps_to_solve_for(3, 1, 2)
