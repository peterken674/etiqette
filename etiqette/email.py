from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name,receiver):
    subject = 'Welcome to the Etiqette.'
    sender = 'dev.ken674@gmail.com'

    text_content = render_to_string('email/newsemail.txt',{"name": name})
    html_content = render_to_string('email/newsemail.html',{"name": name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()

def send_ticket_email(name,receiver, ticket, num_seats, cost, session, movie):
    subject = 'Ticket #'+ticket+ ' successfuly bought.'
    sender = 'dev.ken674@gmail.com'

    text_content = render_to_string('email/ticket.txt',{
        "ticket": ticket,
        "num_seats": num_seats,
        "cost":cost,
        "name":name,
        "session":session,
        "movie":movie
        })
    html_content = render_to_string('email/ticket.html',{
        "ticket": ticket,
        "num_seats": num_seats,
        "cost":cost,
        "name":name,
        "session":session,
        "movie":movie
        })

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()