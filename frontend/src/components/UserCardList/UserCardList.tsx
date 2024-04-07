import { ReactElement } from 'react';
import { ISubscription } from '../../utils/interfaces/interfaces';
import UserCard from '../SubscriptionCard/SubscriptionCard';
import { styled } from 'styled-components';

interface IUserCardListProps {
  cardsList: ISubscription[];
}

const Section = styled.section`
  padding-top: 20px;
`;

export default function UserCardList(props: IUserCardListProps): ReactElement {
  const cardsList = props.cardsList.map((card, index) => (
    <UserCard card={card} key={`user-card-${index}`} />
  ));

  return <Section>{cardsList}</Section>;
}
