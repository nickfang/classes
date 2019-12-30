import Link from 'next/Link';

const Home = props => (
    <div>
        <p>Hey!</p>
        <Link href="/sell">
            <a>Sell</a>
        </Link>
    </div>
);

export default Home;