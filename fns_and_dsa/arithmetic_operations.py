def perform_operation(num1, num2, operation):
  match operation:
    case _ if operation ==  'add':
      return num1 + num2
    case _ if operation ==  'subtract':
      return num1 - num2
    case _ if operation == 'multiply':
      return num1 * num2
    case _ if operation ==  'divide':
      if num2 > 0:
        return num1 / num2
      else:
        return
