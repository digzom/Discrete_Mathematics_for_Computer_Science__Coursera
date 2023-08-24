defmodule GuessingGame do
  def guess(lower, upper) do
    middle = div(lower + upper, 2)

    answer = CleanInput.gets("Is x = #{middle}? (equal, smaller, greater) \n")

    case answer do
      "equal" ->
        IO.puts("\nThanks for playing!")

      "smaller" ->
        guess(lower, middle - 1)

      "greater" ->
        guess(middle + 1, upper)

      invalid_answer ->
        IO.puts("\n\u001b[1m'#{invalid_answer}' is not a valid answer\u001b[0m\n")
        guess(lower, upper)
    end
  end
end

# defmodule GuessingGame do
#   def guess(lower, upper) do
#     middle = div(lower + upper, 2)

#     answer = CleanInput.gets("Is x = #{middle}? (equal, smaller, greater) \n")

#     continue_or_finish(answer, lower, upper, middle)
#   end

#   defp continue_or_finish("equal", _, _, _), do: IO.puts("\nThanks for playing!")
#   defp continue_or_finish("smaller", lower, _upper, middle), do: guess(lower, middle - 1)
#   defp continue_or_finish("greater", _lower, upper, middle), do: guess(middle + 1, upper)

#   defp continue_or_finish(answer, lower, upper, _middle) do
#     IO.puts("\n\u001b[1m'#{answer}' is not a valid answer\u001b[0m\n")
#     guess(lower, upper)
#   end
# end

defmodule CleanInput do
  def gets(text) do
    text
    |> IO.gets()
    |> String.replace("\n", "")
  end
end

lower =
  CleanInput.gets("What will be the \u001b[1m\u001b[31msmallest\u001b[0m number? ")
  |> String.to_integer()

upper =
  CleanInput.gets("And the \u001b[1m\u001b[31mgreater\u001b[0m one? ") |> String.to_integer()

GuessingGame.guess(lower, upper)
