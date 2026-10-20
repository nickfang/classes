const ROLES = ['admin', 'staff', 'editor', 'member', 'viewer'] as const;

type Role = (typeof ROLES)[number]
export type User = {
    id: number,
    name: string,
    email: string,
    role: Role,
    createdAt: Date
}



const roleLabel: Record<Role, string> = {
    'admin': 'admin',
    'staff': 'staff',
    'editor': 'editor',
    'member': 'member',
    'viewer': 'viewer',
}

type UserCard = Pick<User, 'name' | 'email'> 

export const users: User[] = [
    {
        id: 1,
        name: 'user1',
        email: 'user1@test.com',
        role: 'admin',
        createdAt: new Date(),
    },
    {
        id: 2, 
        name: 'user2',
        email: 'user2@test.com',
        role: 'staff',
        createdAt: new Date(),
    },
    {
        id: 3, 
        name: 'user3',
        email: 'user3@test.com',
        role: 'staff',
        createdAt: new Date(),
    },
    {
        id: 4, 
        name: 'user4',
        email: 'user4@test.com',
        role: 'staff',
        createdAt: new Date(),
    },
    {
        id: 5, 
        name: 'user5',
        email: 'user5@test.com',
        role: 'staff',
        createdAt: new Date(),
    }
]

const userCards: UserCard[] = users.map(({name, email}) => ({name, email}))




console.log(roleLabel, userCards);