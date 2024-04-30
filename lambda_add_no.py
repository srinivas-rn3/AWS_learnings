def lambda_function(event,context):
    # Get the numbers from the event
    num1 = event['num1']
    num2 = event['num2']
    # Calculate the sum
    result = num1 +num2
    # Return the result
    return{
        'statusCode':200,
        'body':{
            result:result
        }
    }