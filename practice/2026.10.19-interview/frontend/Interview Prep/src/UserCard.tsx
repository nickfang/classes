import type { User } from "./roles"
import { users } from "./roles"
import styles from "./UserCard.module.css"

type UserCard = Pick<User, "name" | "email">

export const UserCard = () => {
  const cardUsers: UserCard[] = users

  return (
    <>
      <h1>UserCards</h1>
      <div className={styles.container}>
        {
          cardUsers.map(item => {
            return (
              <div className={styles.card}>
                <div>{item.name}</div>
                <div>{item.email}</div>
              </div>
            )
          })
        }
      </div>
    </>
  )
}
