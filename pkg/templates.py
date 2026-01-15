from pkg.dto.schemas import EmailTypeEnum

def _template_reserve(data: dict):
    user = data.get("user_name", "Utente")
    book = data.get("book_title", "un libro")
    return "Conferma Prenotazione", f"Ciao {user}, hai prenotato '{book}'."

def _template_return(data: dict):
    user = data.get("user_name", "Utente")
    book = data.get("book_title", "un libro")
    return "Restituzione Avvenuta", f"Grazie {user}, hai restituito '{book}'."

EMAIL_TEMPLATES = {
    EmailTypeEnum.RESERVE: _template_reserve,
    EmailTypeEnum.RETURN: _template_return,

}