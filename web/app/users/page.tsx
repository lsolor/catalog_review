
export default function CreateUser() {
    fetch(process.env.NEXT_PUBLIC_API_BASE_URL + '/users', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            username: 'newuser',
            email: 'newuser@example.com',
        }),
    });
    // Need to handle response and errors in a real application
    // render a simple confirmation message for now
    return (
    <div className="font-sans grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20">
      <main className="flex flex-col gap-[32px] row-start-2 items-center sm:items-start">
        <h1 className="text-2xl font-bold">Create User Page</h1>
      </main>
    </div>
  );
}