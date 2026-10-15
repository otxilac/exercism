def response(hey_bob) -> str:
    """Determines what Bob will reply to someone when they say something to him or ask him a question."""
    message: str = hey_bob.strip()
    
    if message == "":
        return "Fine. Be that way!"
    elif message.isupper() and message.endswith("?"):
        return "Calm down, I know what I'm doing!"
    elif message.isupper():
        return "Whoa, chill out!"
    elif message.endswith("?"):
        return "Sure."
    else:
        return "Whatever."
    
    
