from database import Database
from models import Contact

def display_menu():
    print("\nGerenciador de Contatos")
    print("1. Adicionar Contato")
    print("2. Ver Contatos")
    print("3. Editar Contato")
    print("4. Remover Contato")
    print("5. Buscar Contato")
    print("6. Sair")

def main():
    db = Database("contacts.db")
    
    while True:
        display_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            name = input("Digite o nome do contato: ")
            phone = input("Digite o telefone do contato: ")
            email = input("Digite o e-mail do contato: ")
            contact = Contact(name, phone, email)
            db.add_contact(contact)
            print("Contato adicionado!")
        elif escolha == '2':
            contacts = db.get_all_contacts()
            if contacts:
                print("\nContatos:")
                for contact in contacts:
                    print(f"ID {contact[0]}: Nome: {contact[1]}, Telefone: {contact[2]}, E-mail: {contact[3]}")
            else:
                print("Nenhum contato encontrado.")
        elif escolha == '3':
            contact_id = input("Digite o ID do contato para editar: ")
            contact = db.get_contact_by_id(contact_id)
            if contact:
                print(f"Contato Atual: Nome: {contact[1]}, Telefone: {contact[2]}, E-mail: {contact[3]}")
                new_name = input("Digite o novo nome (ou pressione Enter para manter o atual): ")
                new_phone = input("Digite o novo telefone (ou pressione Enter para manter o atual): ")
                new_email = input("Digite o novo e-mail (ou pressione Enter para manter o atual): ")
                contact = Contact(
                    new_name if new_name else contact[1],
                    new_phone if new_phone else contact[2],
                    new_email if new_email else contact[3]
                )
                db.update_contact(contact_id, contact)
                print("Contato atualizado!")
            else:
                print("Contato não encontrado.")
        elif escolha == '4':
            contact_id = input("Digite o ID do contato para remover: ")
            db.delete_contact(contact_id)
            print("Contato removido!")
        elif escolha == '5':
            search_term = input("Digite o nome ou parte do nome para buscar: ")
            contacts = db.search_contacts(search_term)
            if contacts:
                print("\nResultados da Busca:")
                for contact in contacts:
                    print(f"ID {contact[0]}: Nome: {contact[1]}, Telefone: {contact[2]}, E-mail: {contact[3]}")
            else:
                print("Nenhum contato encontrado.")
        elif escolha == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
