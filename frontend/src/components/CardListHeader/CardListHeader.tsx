import { ReactElement } from 'react';
import { Link } from 'react-router-dom';
import './CardListHeader.scss';


interface CardListHeaderProps {
  title: string;
  link: string;
}

function CardListHeader(props: CardListHeaderProps): ReactElement {
  return (
    <div className="card-list-header">
      <h2>{ props.title }</h2>
      <Link className="link" to={ `${ props.link }` }>Все</Link>
    </div>
  );
}

export default CardListHeader;
