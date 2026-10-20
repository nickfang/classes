type DefaultUsers = "John" | "Jane";
type Role = "admin" | "member";

type User = { id: string; name: string; email: string; role: Role };
type PartialType = Partial<User>;
type PickType = Pick<User, "id" | "name">;
type OmitType = Omit<User, "name">;
type RecordType = Record<DefaultUsers, Role>;
type ReturnTypeType = ReturnType<() => User>;

let a;
let b: PartialType;
let c: PickType;
let d: OmitType;
let e: RecordType = {
    "John": "admin",
    "Jane": "member",
};
let f = (): ReturnTypeType => {
    return {
        id: "3",
        name: "test3",
        email: "test3@test.com",
        role: "admin",
    }
};

a = { id: "1", name: "test", email: "test@test.com", role: "admin" } 
b = {}
c = { id: "1", name: "test" }
d = { id: "2", email: "test@test.com", role: "admin"}



console.log(a);
console.log(b);
console.log(c);
console.log(d);
console.log(e);
console.log(f());
