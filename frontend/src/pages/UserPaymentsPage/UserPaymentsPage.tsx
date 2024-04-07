import { ReactElement } from 'react';
import styled from 'styled-components';
import UserCardList from '../../components/UserCardList/UserCardList';
import { useSelectorTyped } from '../../hooks/store';
import PaymentCard from '../../components/PaymentCard/PaymentCard';

const Title = styled.h1`
  font-size: 24px;
  font-weight: 600;
  text-align: left;
`;

const PaymentsList = styled.ul`
  list-style: none;
  padding: 0;
  margin: 0;
`

export default function UserPaymentsPage(): ReactElement {
  const paymentsList = useSelectorTyped(
    (store) => store.currentUserReducer.paymentHistory
  );

  return (
    <section>
      <Title>История платежей</Title>
      <PaymentsList>
        {paymentsList.map((item, index) => (
          <li key={`payment-${index}`}>
            <PaymentCard card={item}/>
          </li>
        ))}
      </PaymentsList>
    </section>
  );
}
